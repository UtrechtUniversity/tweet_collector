# Search tweet
In this package we address two types of queries. Type of query should be set in the config file.
## Full Archive Search
Query the complete archive of public Tweets created since the first Tweet in March 2006 (N.B. Only available for [**Academic Research**](https://developer.twitter.com/en/docs/projects/overview#product-track) developer accounts).

## Current Search
Query the most recent seven days of Tweets, and receive full-fidelity responses with this first release of our search Tweets functionality.
  

Example
```
cd tweet_collector
python3 src/search_tweet.py --credential-file "config/.twitter_keys.yaml" --config-file "config/api_config.config 

```


