# IGQL

- Metadata
    - References
        - [https://github.com/FKLC/IGQL](https://github.com/FKLC/IGQL)
    - Announcements

        ![IGQL%200fb5b3b79d6a4c3e938953497d98fad8/Untitled.png](IGQL%200fb5b3b79d6a4c3e938953497d98fad8/Untitled.png)

> Iterating quickly with IGQL: A new domain-specific language

Building the optimal recommendation algorithms and techniques is an ongoing area of research in the ML community, and the process of choosing the right system can vary widely depending on the task. For instance, while one algorithm may effectively identify long-term interests, another may perform better at identifying recommendations based on recent content. Our engineering team iterates on different algorithms, and we needed a way for us to both try out new ideas efficiently and apply the promising ideas to large-scale systems easily without worrying too much about computational resource implications like CPU and memory usage. We needed a custom domain specific meta-language that provides the right level of abstraction and assembles all algorithms into one place.

To solve this, we created and shipped IGQL, a domain-specific language optimized for retrieving candidates in recommender systems. Its execution is optimized in C++, which helps minimize both latency and compute resources. It’s also extensible and easy to use when testing new research ideas. IGQL is both statically validated and high-level. Engineers can write recommendation algorithms in a Python-like way and execute fast and efficiently in C++.

```graphql
user 
.let(seed_id=user_id) 
.liked(max_num_to_retrieve=30) 
.account_nn(embedding_config=default) 
.posted_media(max_media_per_account=10) 
.filter(non_recommendable_model_threshold=0.2) 
.rank(ranking_model=default) 
.diversify_by(seed_id, method=round_robin)
```

In the code sample above, you can see how IGQL provides high readability even for engineers who haven’t worked extensively in the language. It helps assemble multiple recommendation stages and algorithms in a principled way. For example, we can optimize the ensemble of candidate generators by using a combiner rule in query to output a weighted blend of several subquery outputs. By tweaking their weights, we can find the combination that results in the best user experience.

IGQL makes it simple to perform tasks that are common in complex recommendation systems, such as building nested trees of combiner rules. IGQL lets engineers focus on ML and business logic behind recommendations as opposed to logistics, like fetching the right quantity of candidates for each query. It also provides a high degree of code reusability. For instance, applying a ranker is as simple as adding a one-line rule to our IGQL query. It’s trivial to add it in multiple places, like ranking accounts and ranking media posted by those accounts.