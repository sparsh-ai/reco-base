
from surprise import KNNWithMeans
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise import Reader

ratings = pd.read_csv('./data/ml-latest-small/ratings.csv')
ratings.head()

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# KNN with mean - Run 10-fold cross-validation and print results
algo = KNNWithMeans(k=50, verbose=False)
cv = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=10, verbose=False)

Avg_RMSE = []
Avg_MAE = []

rmse_mean =  cv['test_rmse'].mean()
mae_mean = cv['test_mae'].mean()

Avg_RMSE.append(rmse_mean) 
Avg_MAE.append(mae_mean)

cv['test_rmse'].mean(), cv['test_mae'].mean()