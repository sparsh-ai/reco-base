Amazon exposes the official datasets (http://jmcauley.ucsd.edu/data/amazon/) which have filtered out users and items with less than 5 reviews and removed a large amount of invalid data. Because of above advantages, these datasets are widely utilized by researchers.

### Strategy 1
- Source: https://github.com/TsingZ0/TLSAN/tree/master/utils
- Sequence: download.sh -> convert.py -> remap.py
- Strategy:
  - Remove the users whose interactions less than 10 and the items which interactions less than 8 to ensure the effectiveness of each user and item.
  - Select the users with more than 4 sessions, and select up to 90 behavior records for the remaining users. This step guarantees the existence of long- and short-term behavior records and all behavior records occurred within recent three months.
