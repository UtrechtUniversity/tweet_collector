# Search Tweets

Twitter forms a rich source of information for researchers interested in studying 'the public conversation'. In this guideline, we will describe how you can use the [tweet_collector repository](https://github.com/UtrechtUniversity/tweet_collector) to extract tweets for *your* research!

## Quick start
- Navigate to the `tweet_collector` directory. In ResearchCloud you should go to `File System/opt/tweet_collector`.
- Go to `config` directory and select `View/ show hidden files` to show hidden files. 
- Remove  `.TEMPLATE` from the extension of `.twitter_keys.yaml` and `api_config.config`.
- Open `.twitter_keys.yaml` and add your credentials in `consumer_key`, `consumer_secret` and `bearer_token`
- Open `api_config.config` and fill in your search query. For more details go to `Configuration file` in `Settings` section.
- Open a terminal and navigate to `tweet_collector`. In ResearchCloud you should type `cd ../../opt/tweet_collector`. 
- If you run the application locally, make sure you activate the virtual environment that you setup for tweet_collector.
- Run the `tweet_collector` command to start collecting the tweets.

**Notes**
To find more details read the `Settings` section.


## Settings

In order to search tweets using tweet_collector, you need to set the **endpoint**, **credentials**, and **configurations**.

### 1. Endpoint
In order to find Tweets related to the topic of your interest, you may search tweets using two endpoints, **recent search** ,or **full-archive search**. A recent search will yield Tweets from the **past 7 days**, while the full-archive search goes back to the first public Tweet from **March 2006**. 

Please keep in your mind that **full-archive search is accessible only through the Academic Research product track.** If you do not have access to an Academic Research account, you still can poll or listen to tweets using a [standard product track](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction).  

By default, this library expects to find the endpoint in `config/.twitter_keys.yaml`. 

Note: Please keep in your mind that '.twitter_keys.yaml' is a hidden file. To read such a file you go to that folder and press Ctrl + H . You will see all hidden files, along with regular files that are not hidden.

#### 1.A. Recent Search
To execute a recent search, the endpoint specification needs to be set to 'recent'. The ‘recent’ search endpoint provides Tweets from the **past 7 days**. To use recent search endpoint, copy the following code in `.twitter_keys.yaml`.

```
search_tweets_v2:
  endpoint:  https://api.twitter.com/2/tweets/search/recent

```

#### 1.B. Full-archive Search
To execute a full-archive search, the endpoint specification needs to be set to 'all'. This endpoint provides access to all publicly available Tweets posted **since March 2006**. To use the full-archive search endpoint, copy the following code in `.twitter_keys.yaml`.

```
search_tweets_v2:
  endpoint:  https://api.twitter.com/2/tweets/search/all
```

### 2. Credentials
The credential file holds your Twitter credentials. They can be set either as environment variables or in a yaml file that includes the endpoint.(i.e., `.twitter_keys.yaml`). An example of such a credential file can be found at `config/.twitter_keys.yaml.TEMPLATE`:

* The simplest credential file should look like this:
```
search_tweets_v2:
  endpoint:  https://api.twitter.com/2/tweets/search/...
  consumer_key: ek...
  consumer_secret: hy...
  bearer_token: AA...
```

OR 


* To set credentials as environment variables, run the following code in **Terminal**:
```
export consumer_key=[ek...]
export consumer_secret=[hy...]
export bearer_token=[AA...]
```

### 3. Configuration file
The configuration file generally contains three groups of elements: **search rules (including search query)**, **search paramters**, and **output paramters**. If a valid configuration file is found, all arguments will be populated from there. 


An example of such a config-file can be found at `config/api_config.config.TEMPLATE`:

```
[search_rules]
start_time = 2020-05-01
end_time = 2021-06-01
query = (happy OR happiness) lang:en -birthday -is:retweet has:geo has:media
tweet_fields = id,author_id,text,created_at
place_fields = contained_within,country
media_fields = type,preview_image_url
expansions = geo.place_id,attachments.media_keys,author_id

[search_params]
results_per_call = 10
max_tweets = 10
output_format = r

[output_params]
save_file = True
filename_prefix = output_new
results_per_file = 10
```

In the following you can find more details about each section.

#### 3.A. Search rules
As the name suggests, the `[search_rules]` should contain all search filters necessary for your research. 

##### Time/id filters
To filter Tweets based on time/id, use one or more of the following search rules:
```
start_time = <Start of datetime window, format ‘YYYY-mm-DDTHH:MM’> 
end_time = <End of datetime window, format ‘YYYY-mm-DDTHH:MM’>
since_id = <Tweet ID, will start search from Tweets after this one>
until_id = <Tweet ID, will end search from Tweets before this one>
```
*Example: if you want to look back for relevant Tweets till may 2021, you can use `start_time = 2021-05-01`*

##### Adding extra info
To include extra information to your results, you can use various **'..._fields'** rules (see [this page](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) for more info):
```
tweet_fields = <A comma-delimited list of Tweet JSON attributes to include in endpoint responses>
place_fields = <A comma-delimited list of Twitter Place JSON attributes to include in endpoint responses>
user_fields = <A comma-delimited list of User JSON attributes to include in endpoint responses>
media_fields = <A comma-delimited list of media JSON attributes to include in endpoint responses>
poll_fields = <A comma-delimited list of Twitter Place JSON attributes to include in endpoint responses>
```
*Example: if you want to know more about the geographical information of the filtered tweets, such as the country and country code, you can include `geo_fields = country,country_code`.*

N.B. To be able to include (one of) these extra fields listed above, you also need to provide the **'expansions'** rule:
```
expansions = <A comma-delimited list of expansions. Specified expansions results in full objects in the ‘includes’ response object>
```
*Example: if you wish to include `geo_fields = country,country_code` you have to include `expansions = geo.place_id`. While the place ID will be located in the Tweet object, you will find this ID and all additional place fields in the 'includes' data object. (Please see [this page](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) for ..._fields-expansions pairs.)*

##### Search query

Finally, the most import rule, is your search query:
```
query = <Search query>
```
In the query specification, you enter how you wish to filter Tweets. Commonly used arugments are:
* `<key_word1> OR <key_word2>`: look for Tweets including either word1 or word2 *(Example: happy OR happiness finds Tweets with the words happy or happiness in them)*
* `lang:<lang>`: only receive Tweets that are in specific langauge *(Example, lang:en selects only English Tweets)*
* `-is:<type>`: '-' is a negation operator; excludes certain types of Tweets *(Example: -is:retweet exclused retweets, leaving only original Tweets)* 
* `-<key_word>`: '-' is a negation operator; excludes Tweets with key_word in it *(Example: -birthday excludes Tweets with 'birthday' in them)*
* `has:<prop>`: matches Tweets that have specific property *(Example: has:geo selectes Tweets with Tweet-specific geolocation data provided by the Twitter user)*

So, if you want to look for original Tweets in English related to happy or happiness containing at least one hashtag, but are not related to birthday whishes, we write:
```
query = (happy OR happiness) lang:en -birthday -is:retweet has:hashtags
```

To get an extensive overview of how you can structure a query, have a look [here](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query). 

#### 3.B. Search parameters
Search parameters determine how the filtering is done and how the final output is structured.

Here are some examples:
```
[search_params]
results_per_call = <Number of results to return per call (default 10; max 100)>
max_tweets = <Maximum number of Tweets to return for this session of requests>
max_pages = <Maximum number of pages/API calls to use for this session>
output_format = <Set output format*>
extra_headers = <JSON-formatted str representing a dict of additional HTTP request headers>
```
*<br>
‘r’ Unmodified API [R]esponses. (default). <br>
‘a’ [A]tomic Tweets: Tweet objects with expansions inline. <br>
‘m’ [M]essage stream: Tweets, expansions, and pagination metadata as a stream of messages.

#### 3.C. Output parameters
The output parameters are the final step of the search; they describe if the output should be stored and how: 

```
[output_params]
save_file = True
filename_prefix = <prefix for the filename where tweet json data will be stored>
results_per_file = <Maximum tweets to save per file>
```
