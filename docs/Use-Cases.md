## Most common
- Popular Products - This is a basic but powerful recommendation logic that works splendidly in nearly all ecommerce stores. The popularity of a product is determined by the number of times it has been purchased (weighted with how long it’s been available). However, more sophisticated recommender systems incorporate other event data into their logics in order to serve even more accurate recommendations (e.g., clicks, views, add-to-cart events, and so on). Getting this right is extremely important, given that the Pareto’s rule in marketing says 80% of product sales come from 20% of products. In the case of content sites (i.e. news sites and video portals), other factors such as time spent on page, percentage scrolled, or seconds watched (of a video) can also be important popularity factors.
- Personalized recommendations - Personalized recommender widgets display different products to each user based on their past purchase and browsing history. Recommendation algorithms used for this task can differ greatly in terms of how they’re implemented and the factors they consider (and often times, “the devil is in the details,” as they say). Nevertheless, as popular product recommendations are good for catering for the mainstream, one of the main benefits of personalization in product recommendations is that they can increase the sales of “long tail” items. However, personalized recommendations require considerable amounts of behavioral data on users, which a system does not have in the case of new visitors. This is called the cold start problem for recommender systems. Personalized collaborative filtering recommendations logic is the most common way of personalized recommendations. It’s focusing on the average similarity of products, to the last X number of products a user has viewed. The system uses the same item-to-item collaborative similarity for this task, but it doesn’t compare one item to another, but to all items in the user’s history. Weighing the output based on the recency of interactions usually improves accuracy further.
- Similar products - Similar product boxes can be based on very different logics. The least complex one is simple category-based filtering, which can be implemented even without a recommendation engine (needless to say, it lags behind in performance as well). If you combine this simple filtering method with meta-data based similarity (descriptions, product titles, tags, prices, etc.), you can greatly enhance the performance, such as by recommending items of the same brand or same color from the current category). For this, you will need to have advanced recommender functionality available on your site. One of the best-performing similarity based logics is a method called “item-to-item collaborative filtering,” a method pioneered by Amazon. I’ll elaborate on this below.
- “Customer who bought/viewed this also bought/viewer” collaborative filtering - Collaborative filtering in ecommerce product recommendations was first implemented at scale by Amazon—they filed their initial patent for item-to-item collaborative filtering as early as 1999. I believe their results speak for themselves. At its core, collaborative filtering works by collecting preferences or taste information from many users (collaborating). Collaborative filtering can fuel item-to-item (product similarity based) and personalized recommendations as well. Item-to-item collaborative filtering recommendation logic basically determines the similarity of two products by looking at how often they’re present together in the browsing or purchase histories of users. In practice, widgets using this kind of logics are named “Customers who viewed this also viewed…” which pretty much explains the basic idea. The preference models these algorithms build are very authentic and specific to your website and your users—they quantify the real interactions between your visitors and platform. Moreover, with ample amount of data, even problems such as automated accessory recommendations can be answered with a reasonable accuracy. (More on this below, in the cart page accessory recommendation section.)
- Recommending accessories - Recommending accessories for products can significantly increase average order size and value on your site. Moreover, implementing such widgets can be quite easy from a technical point of view. However, depending on the size of your catalog and your category structure, it can be relatively admin-heavy, as it is hard to automate the process of recommending compatible accessories for each item. Therefore, such logics are usually fueled by manually assigned item relations. Ideally, you can recommend categories to categories directly (i.e. iPhone -> iPhone Accessories). This is a lot easier to automate and scale, but requires extremely conscious category structure planning. Of course, with enough data and a bit of creativity, one can abstract rules on how to analyze behavioral information, so that the output of the system will be actual, compatible accessories. One of such easily codifiable rules that can define an accessory in relation to a product is items that are often bought together with it, but cost significantly (two times, three times, or more) less. This is a method we utilize at some of our enterprise clients. This is where volume comes into play, as with a few purchases, results generated by this algorithm would be unpredictable, but reaching a critical amount of data, all statistics tend to correlate with reality more and more (given that the premises are correct).
- Frequently bought together - Displaying frequently bought together products on cart pages can be very effective. However, in order for virtually any cart page recommendation to provide results, the checkout process must lead customers through the cart page, where the actual recommendations are featured. It is also a relatively data-heavy recommendation technique. The layout of this page is also an important factor. If you have the time and resources, A/B testing different layouts and designs can yield excellent results and insights. (Needless to say, this holds true globally, not just for recommendations.) Netflix, for instance, uses A/B tests extensively for home screen layouts on different platforms, featured shows, and even movie artworks. There’s certainly a lot to learn form their approach.

## Industry specific
### **e-Commerce**

Industry where recommendation systems were first widely used. With millions of customers and data on their online behavior, e-commerce companies are best suited to generate accurate recommendations

### **Retail**

Target scared shoppers back in 2000s when [Target systems were able to predict pregnancies even before mothers realized their own pregnancies](https://www.nytimes.com/2012/02/19/magazine/shopping-habits.html?pagewanted=1&_r=1&hp). Shopping data is the most valuable data as it is the most direct data point on a customer’s intent. Retailers with troves of shopping data are at the forefront of companies making accurate recommendations

### **Media**

Similar to e-commerce, media businesses are one of the first to jump into recommendations. It is difficult to see a news site without a recommendation system.

### **Banking**

A mass market product that is consumed digitally by millions. Banking for masses and SMEs are prime for recommendations. Knowing a customer’s detailed financial situation, along with their past preferences, coupled by data of thousands of similar users is quite powerful.

### **Telecom**

Shares similar dynamics with banking. Telcos have access to millions of customers whose every interaction is recorded. Their product range is also rather limited compared to other industries, making recommendations in telecom an easier problem.

### **Utilities**

Similar dynamics with telecom but utilities have an even narrower range of products, making recommendations rather simple.

## Other
- Personalised merchandising
- Personalised content
- Search re-ranking
- Related product
- Popular product
- Similar product
- Purchase: People who bought X also bought Y
- Experience: People who read/watched/enjoyed X also enjoyed Y
- Location: People who have been at/ate at/stayed at X also went to Y
- Current website: People who come to this website also browse Y
- Education: People who knew about/worked on/learnt/ X also learnt Y
- Hiring: People who have skills like your employees
- Recipes: People who cooked X also cooked Y
- Context: People in X mood, at Z time do activity Y more
- Finance: Stocks bought by successful X people
- Popularity: Items popular in the last hour, week, year
- Promotions: People who should be offered promotion Y
- Social: People/friends are talking about item Y
- Health: People who are healthy do Y more
- Drugs: People with X characteristics respond to drug Y better
- Ideas: Past ideas/patents/companies related to your idea
- Law: Past cases related to your current lawsuit
- Law Enforcement (slightly scary): People similar to X are likely to commit a crime Y