# reco-base
This repository contains the python code, jupyter notebooks and other essential resources for knowing and building recommender systems.

![recobase logo](https://github.com/sparsh-ai/reco-base/blob/main/utils/images/recobase_logo.png?raw=true)

## Code
Contains python code and jupyter notebooks. Check [this](https://github.com/sparsh-ai/reco-base/wiki/Notebooks) wiki page for full list of notebooks and its associated colab/nbviewer links.

## Documentation
- https://github.com/sparsh-ai/reco-base/wiki
- https://reco-base.readthedocs.io/en/latest
- https://sparsh-ai.github.io/reco-base

## Resources
### Tutorials
- [Feature engineering for recommender systems using Nvidia Merlin on REES46 dataset](https://github.com/rapidsai/deeplearning/tree/15ef56bb5f23e286ab0f907e98ff66d6ff221905/RecSys2020Tutorial) [[video](https://youtu.be/uROvhp7cj6Q)]
- [Reco Tutorials](https://sparsh-ai.github.io/rec-tutorials/)
- [Microsoft Recommenders Library](https://github.com/microsoft/recommenders)
- [RapidsAI Tutorials](https://github.com/rapidsai/deeplearning)
- [Sequence-aware Recommender Workshop](https://github.com/mquad/sars_tutorial)

### Projects
- [RecoFront](https://github.com/sparsh-ai/reco-front)
- [RecoBandit](https://github.com/sparsh-ai/reco-bandit)
- [Recommender Capstone](https://github.com/rachelkoenig10/recommender-system-capstone)
- [Simple recommender with matrix factorization, graph, and NLP on Amazon dataset](https://github.com/eugeneyan/recsys-nlp-graph)

### Blog Posts
- [RecoChef](https://medium.com/recochef)

### Knowledge Sources
* http://www.arxiv-sanity.com/search?q=recommender
* http://www.arxiv-sanity.com/search?q=cs.AI+cs.IR
* [RecBole: A unified, comprehensive and efficient recommendation library](https://recbole.io/)
* https://paperswithcode.com/task/recommendation-systems/latest#code

## Datasets
### Shopping
- [Amazon](http://jmcauley.ucsd.edu/data/amazon/):
This dataset contains product reviews, only-rating data (ratings) and metadata(descriptions, category information, price, brand, and image features) from Amazon, including 142.8 million reviews spanning May 1996 - July 2014.  
- [Epinions](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data):
This dataset was collected from Epinions.com, a popular online consumer review website. It contains trust relationships
amongst users and spans more than a decade, from January 2001 to November 2013.
- [Yelp](https://www.yelp.com/dataset):
This dataset was collected from Yelp.com. The Yelp dataset is a subset of our businesses, reviews,
and user data for use in personal, educational, and academic purposes.
- [Tmall](https://tianchi.aliyun.com/dataset/dataDetail?dataId=53):
This dataset is provided by Ant Financial Services, using in the IJCAI16 contest.
- [DIGINETICA](https://competitions.codalab.org/competitions/11161):
The dataset includes user sessions extracted from an e-commerce search engine logs, with anonymized user ids,
hashed queries, hashed query terms, hashed product descriptions and meta-data, log-scaled prices, clicks, and purchases.
- [YOOCHOOSE](https://2015.recsyschallenge.com/challenge.html):
This dataset was constructed by YOOCHOOSE GmbH to support participants in the RecSys Challenge 2015.
- [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset):
The data has been collected from a real-world ecommerce website. It is raw data, i.e.
without any content transformations, however, all values are hashed due to confidential issues.
- [Ta Feng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset):
The dataset contains a Chinese grocery store transaction data from November 2000 to February 2001.

### Advertising
* [Criteo](https://www.kaggle.com/c/criteo-display-ad-challenge/data):
  This dataset was collected from Criteo, which consists of a portion of Criteo's traffic over a period of several days.
* [Avazu](https://www.kaggle.com/c/avazu-ctr-prediction/data):
  This dataset is used in Avazu CTR prediction contest.
* [iPinYou](http://contest.ipinyou.com): This dataset was provided by iPinYou, which contains all training datasets and leaderboard testing datasets of the three seasons iPinYou Global RTB(Real-Time Bidding) Bidding Algorithm Competition.

### Check-in
* [Foursquare](https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset):
This dataset contains check-ins in NYC and Tokyo collected for about 10 month. Each check-in is associated with
its time stamp, its GPS coordinates and its semantic meaning.
* [Gowalla](https://snap.stanford.edu/data/loc-gowalla.html):
This dataset is from a location-based social networking website where users share their locations by checking-in,
and contains a total of 6,442,890 check-ins of these users over the period of Feb. 2009 - Oct. 2010.

### Movies
- [MovieLens](https://grouplens.org/datasets/movielens/):
GroupLens Research has collected and made available rating datasets from their movie web site.
- [Netflix](https://www.kaggle.com/netflix-inc/netflix-prize-data):
This is the official data set used in the Netflix Prize competition.
- [Douban](https://www.kaggle.com/utmhikari/doubanmovieshortcomments):
Douban Movie is a Chinese website that allows Internet users to share their comments and viewpoints about movies.
This dataset contains more than 2 million short comments of 28 movies in Douban Movie website.

### Music
- [Last.FM](https://grouplens.org/datasets/hetrec-2011/):
This dataset contains social networking, tagging, and music artist listening information from a set of 2K users from Last.fm online music system.
- [LFM-1b](http://www.cp.jku.at/datasets/LFM-1b/):
This dataset contains more than one billion music listening events created by more than 120,000 users of Last.FM.
Each listening event is characterized by artist, album, and track name, and includes a timestamp.
- [Yahoo Music](https://webscope.sandbox.yahoo.com/catalog.php?datatype=r):
This dataset represents a snapshot of the Yahoo! Music community's preferences for various musical artists.

### Books
* [Book-Crossing](http://www2.informatik.uni-freiburg.de/~cziegler/BX/):
This dataset was collected by Cai-Nicolas Ziegler in a 4-week crawl (August / September 2004) from
the [Book-Crossing](http://www.bookcrossing.com/) community with kind permission from Ron Hornbaker,
CTO of [Humankind Systems](http://www.humankindsystems.com/). It contains 278,858 users
(anonymized but with demographic information) providing 1,149,780 ratings (explicit / implicit) about 271,379 books.

### Games
* [Steam](https://github.com/kang205/SASRec):
This dataset is reviews and game information from Steam, which contains 7,793,069 reviews, 2,567,538 users,
and 32,135 games. In addition to the review text, the data also includes the users' play hours in each review.

### Anime
- [Anime](https://www.kaggle.com/CooperUnion/anime-recommendations-database):
This dataset contains information on user preference data from myanimelist.net. Each user is able to add anime to
their completed list and give it a rating and this dataset is a compilation of those ratings.

### Pictures
* [Pinterest](https://github.com/hexiangnan/neural_collaborative_filtering/tree/master/Data):
This dataset is originally constructed by paper Learning image and user features for recommendations in social networks
for evaluating content-based image recommendation, and processed by paper Neural Collaborative Filtering.

### Jokes
* [Jester](http://eigentaste.berkeley.edu/dataset/):
This dataset contains anonymous ratings of jokes by users of the Jester Joke Recommender System.

### Exercises
* [KDD2010](https://pslcdatashop.web.cmu.edu/KDDCup/downloads.jsp):
This dataset was released in KDD Cup 2010 Educational Data Mining Challenge,
which contains the situations of students submitting exercises on the systems.

### Websites
* [Phishing Websites](http://archive.ics.uci.edu/ml/datasets/Phishing+Websites):
This dataset contains 30 kinds of features of 11,055 websites and labels of whether they are phishing websites or not.
The websites' features includes 12 address-bar based features, 6 abnormal based features, 5 HTML-and-JavaScript based
features and 7 domain based features.

### Adult
* [Adult](http://archive.ics.uci.edu/ml/datasets/Adult):
This dataset is extracted by Barry Becker from the 1994 Census database, which consists of a list of
people's attributes and whether they make over 50k a year.

### News
* [MIND](https://msnews.github.io/)
This dataset is a large-scale dataset for news recommendation research. It was collected from anonymized behavior logs 
of Microsoft News website. MIND contains about 160k English news articles and more than 15 million impression logs 
generated by 1 million users.
