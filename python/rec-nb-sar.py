#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Simple Algorithm for Recommendation (SAR) is a fast and scalable algorithm 
for personalized recommendations based on user transaction history. It produces 
easily explainable and interpretable recommendations and handles "cold item" 
and "semi-cold user" scenarios. SAR is a kind of neighborhood based algorithm 
(as discussed in Recommender Systems by Aggarwal) which is intended for ranking 
top items for each user. More details about SAR can be found in the deep dive 
notebook.

SAR recommends items that are most similar to the ones that the user already 
has an existing affinity for. Two items are similar if the users that interacted 
with one item are also likely to have interacted with the other. A user has an 
affinity to an item if they have interacted with it in the past.

Advantages of SAR:
High accuracy for an easy to train and deploy algorithm
Fast training, only requiring simple counting to construct matrices used at prediction time.
Fast scoring, only involving multiplication of the similarity matrix with an affinity vector
Notes to use SAR properly:
Since it does not use item or user features, it can be at a disadvantage against algorithms that do.
It's memory-hungry, requiring the creation of an mxm sparse square matrix (where m is the number of items). This can also be a problem for many matrix factorization algorithms.
SAR favors an implicit rating scenario and it does not predict ratings.'''

import logging
import numpy as np
import pandas as pd
from sklearn.preprocessing import minmax_scale

from reco_utils.common.python_utils import binarize
from reco_utils.common.timer import Timer
from reco_utils.dataset.python_splitters import python_stratified_split
from reco_utils.evaluation.python_evaluation import (
    map_at_k,
    ndcg_at_k,
    precision_at_k,
    recall_at_k,
    rmse,
    mae,
    logloss,
    rsquared,
    exp_var
)
from reco_utils.recommender.sar import SAR

# top k items to recommend
TOP_K = 10

# Select MovieLens data size: 100k, 1m, 10m, or 20m
MOVIELENS_DATA_SIZE = '100k'

ratings = pd.read_csv('./data/ml-100k/ratings.csv')
ratings.columns = ["userID", "itemID", "rating", "timestamp"]
# ratings.head()

train, test = python_stratified_split(ratings, ratio=0.75, col_user='userID', col_item='itemID', seed=42)

# print("""
# Train:
# Total Ratings: {train_total}
# Unique Users: {train_users}
# Unique Items: {train_items}

# Test:
# Total Ratings: {test_total}
# Unique Users: {test_users}
# Unique Items: {test_items}
# """.format(
#     train_total=len(train),
#     train_users=len(train['userID'].unique()),
#     train_items=len(train['itemID'].unique()),
#     test_total=len(test),
#     test_users=len(test['userID'].unique()),
#     test_items=len(test['itemID'].unique()),
# ))

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)-8s %(message)s')

model = SAR(
    col_user="userID",
    col_item="itemID",
    col_rating="rating",
    col_timestamp="timestamp",
    similarity_type="jaccard", 
    time_decay_coefficient=30, 
    timedecay_formula=True,
    normalize=True
)

with Timer() as train_time:
    model.fit(train)

# print("Took {} seconds for training.".format(train_time.interval))

with Timer() as test_time:
    top_k = model.recommend_k_items(test, remove_seen=True)

# print("Took {} seconds for prediction.".format(test_time.interval))

# top_k.head()

eval_map = map_at_k(test, top_k, col_user='userID', col_item='itemID', col_rating='rating', k=TOP_K)
eval_ndcg = ndcg_at_k(test, top_k, col_user='userID', col_item='itemID', col_rating='rating', k=TOP_K)
eval_precision = precision_at_k(test, top_k, col_user='userID', col_item='itemID', col_rating='rating', k=TOP_K)
eval_recall = recall_at_k(test, top_k, col_user='userID', col_item='itemID', col_rating='rating', k=TOP_K)
eval_rmse = rmse(test, top_k, col_user='userID', col_item='itemID', col_rating='rating')
eval_mae = mae(test, top_k, col_user='userID', col_item='itemID', col_rating='rating')
eval_rsquared = rsquared(test, top_k, col_user='userID', col_item='itemID', col_rating='rating')
eval_exp_var = exp_var(test, top_k, col_user='userID', col_item='itemID', col_rating='rating')

positivity_threshold = 2
test_bin = test.copy()
test_bin['rating'] = binarize(test_bin['rating'], positivity_threshold)

top_k_prob = top_k.copy()
top_k_prob['prediction'] = minmax_scale(
    top_k_prob['prediction'].astype(float)
)

eval_logloss = logloss(test_bin, top_k_prob, col_user='userID', col_item='itemID', col_rating='rating')

# print("Model:\t",
#       "Top K:\t%d" % TOP_K,
#       "MAP:\t%f" % eval_map,
#       "NDCG:\t%f" % eval_ndcg,
#       "Precision@K:\t%f" % eval_precision,
#       "Recall@K:\t%f" % eval_recall,
#       "RMSE:\t%f" % eval_rmse,
#       "MAE:\t%f" % eval_mae,
#       "R2:\t%f" % eval_rsquared,
#       "Exp var:\t%f" % eval_exp_var,
#       "Logloss:\t%f" % eval_logloss,
#       sep='\n')

# Now let's look at the results for a specific user
user_id = 876

ground_truth = test[test['userID']==user_id].sort_values(by='rating', ascending=False)[:TOP_K]
prediction = model.recommend_k_items(pd.DataFrame(dict(userID=[user_id])), remove_seen=True) 
pd.merge(ground_truth, prediction, on=['userID', 'itemID'], how='left')