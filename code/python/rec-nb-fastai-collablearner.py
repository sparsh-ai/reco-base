#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import itertools
import numpy as np
import pandas as pd

import torch, fastai
from fastai.collab import EmbeddingDotBias, collab_learner, CollabDataBunch, load_learner

from reco_utils.dataset.python_splitters import python_stratified_split
from reco_utils.recommender.fastai.fastai_utils import cartesian_product, score
from reco_utils.evaluation.python_evaluation import map_at_k, ndcg_at_k, precision_at_k, recall_at_k
from reco_utils.evaluation.python_evaluation import rmse, mae, rsquared, exp_var

USER, ITEM, RATING, TIMESTAMP, PREDICTION, TITLE = 'UserId', 'MovieId', 'Rating', 'Timestamp', 'Prediction', 'Title'

# top k items to recommend
TOP_K = 10

# select movieLens data size: 100k, 1m, 10m, or 20m
MOVIELENS_DATA_SIZE = '100k'

# model parameters
N_FACTORS = 40
EPOCHS = 5

ratings = pd.read_csv('./data/ml-100k/ratings.csv')

# split the dataset
train_valid_df, test_df = python_stratified_split(ratings_df, 
                                                  ratio=0.75, 
                                                  min_rating=1, 
                                                  filter_by="item", 
                                                  col_user=USER, 
                                                  col_item=ITEM )

data = CollabDataBunch.from_df(train_valid_df, 
                               user_name=USER, 
                               item_name=ITEM, 
                               rating_name=RATING, 
                               valid_pct=0)
# data.show_batch()

"""Now we will create a `collab_learner` for the data, which by default uses 
the `EmbeddingDotBias` model. We will be using 40 latent factors. This will 
create an embedding for the users and the items that will map each of these 
to 40 floats as can be seen below. Note that the embedding parameters are not 
predefined, but are learned by the model.

Although ratings can only range from 1-5, we are setting the range of possible 
ratings to a range from 0 to 5.5 -- that will allow the model to predict values 
around 1 and 5, which improves accuracy. Lastly, we set a value for weight-decay 
for regularization."""

learn = collab_learner(data, n_factors=N_FACTORS, y_range=[0,5.5], wd=1e-1)
# learn.model

# Now train the model for 5 epochs setting the maximal learning rate. 
# The learner will reduce the learning rate with each epoch using cosine annealing
learn.fit_one_cycle(EPOCHS, max_lr=5e-3)

# save the learner
learn.export('movielens_model.pkl')


## EVALUATION

# load the learner
learner = load_learner(path=".", file='movielens_model.pkl')

# get all users and items that the model knows
total_users, total_items = learner.data.train_ds.x.classes.values()
total_items = total_items[1:]
total_users = total_users[1:]

# get all users from the test set and remove any users that were now in the training set
test_users = test_df[USER].unique()
test_users = np.intersect1d(test_users, total_users)

# build the cartesian product of test set users and all items known to the model
users_items = cartesian_product(np.array(test_users),np.array(total_items))
users_items = pd.DataFrame(users_items, columns=[USER,ITEM])

# remove the user/items combinations that are in the training set
# we don't want to propose a movie that the user has already watched
training_removed = pd.merge(users_items, train_valid_df.astype(str), on=[USER, ITEM], how='left')
training_removed = training_removed[training_removed[RATING].isna()][[USER, ITEM]]

# score the model to find the top K recommendation
top_k_scores = score(learner, 
                     test_df=training_removed,
                     user_col=USER, 
                     item_col=ITEM, 
                     prediction_col=PREDICTION)

# MAP
eval_map = map_at_k(test_df, top_k_scores, col_user=USER, col_item=ITEM, 
                    col_rating=RATING, col_prediction=PREDICTION, 
                    relevancy_method="top_k", k=TOP_K)

# NDCG
eval_ndcg = ndcg_at_k(test_df, top_k_scores, col_user=USER, col_item=ITEM, 
                      col_rating=RATING, col_prediction=PREDICTION, 
                      relevancy_method="top_k", k=TOP_K)

# Precision
eval_precision = precision_at_k(test_df, top_k_scores, col_user=USER, col_item=ITEM, 
                                col_rating=RATING, col_prediction=PREDICTION, 
                                relevancy_method="top_k", k=TOP_K)

# Recall
eval_recall = recall_at_k(test_df, top_k_scores, col_user=USER, col_item=ITEM, 
                          col_rating=RATING, col_prediction=PREDICTION, 
                          relevancy_method="top_k", k=TOP_K)

# print("Model:\t" + learn.__class__.__name__,
#       "Top K:\t%d" % TOP_K,
#       "MAP:\t%f" % eval_map,
#       "NDCG:\t%f" % eval_ndcg,
#       "Precision@K:\t%f" % eval_precision,
#       "Recall@K:\t%f" % eval_recall, sep='\n')

# calculate scores for test user-item pairs
scores = score(learner, 
               test_df=test_df.copy(), 
               user_col=USER, 
               item_col=ITEM, 
               prediction_col=PREDICTION)

# calculate some regression metrics
eval_r2 = rsquared(test_df, scores, col_user=USER, col_item=ITEM, col_rating=RATING, col_prediction=PREDICTION)
eval_rmse = rmse(test_df, scores, col_user=USER, col_item=ITEM, col_rating=RATING, col_prediction=PREDICTION)
eval_mae = mae(test_df, scores, col_user=USER, col_item=ITEM, col_rating=RATING, col_prediction=PREDICTION)
eval_exp_var = exp_var(test_df, scores, col_user=USER, col_item=ITEM, col_rating=RATING, col_prediction=PREDICTION)

# print("Model:\t" + learn.__class__.__name__,
#       "RMSE:\t%f" % eval_rmse,
#       "MAE:\t%f" % eval_mae,
#       "Explained variance:\t%f" % eval_exp_var,
#       "R squared:\t%f" % eval_r2, sep='\n')