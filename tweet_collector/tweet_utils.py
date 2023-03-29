import pandas as pd
from multiprocessing import Pool
import json
from pathlib import Path
import psutil


def chunks(lst, n):
    """
        Split a list into chunks including n items.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


def save_chunk(argstuple):
    """
    Save a chunk in format of json and csv
    """
    chunk = argstuple[0]
    filename_prefix_org = argstuple[1]
    indx = argstuple[2]
    filename_prefix = filename_prefix_org + '_' + str(indx)

    # Check if filename_prefix contains folder + create it if necessary
    if Path(filename_prefix).parent != Path():
        folder = Path(filename_prefix).parent
        folder.mkdir(parents=True, exist_ok=True)

    # Save a chunk as .json
    with open(filename_prefix + '.json', 'a', encoding='utf-8') as f:
        for ch in chunk:
            json.dump(ch, f)
            f.write('\n')

    # Save all chunks as .csv
    df = pd.DataFrame(chunk)
    df.to_csv(filename_prefix + '.csv', index=False, sep=';')

    print('Status Update based on {}'.format(filename_prefix))


def merge_data_includes(tweets_data, tweets_include):
    """
        Merges tweet object with other objects, i.e. media, places, users etc
    """

    df_tweets_tmp = pd.DataFrame(tweets_data)

    # Add key-values of a nested dictionary in df_tweets_tmp as new columns
    df_tweets = flat_dict(df_tweets_tmp)

    for incl in tweets_include:
        df_incl = pd.DataFrame(tweets_include[incl])
        if incl == 'media':
            # Split each row to multiple rows for each item in media_keys list
            df_incl = df_incl.drop_duplicates(subset=['media_key'])
            df_tweets = df_tweets.explode('media_keys')
            df_tweets = pd.merge(df_tweets, df_incl, how='left', left_on=['media_keys'], right_on=['media_key'],
                                 suffixes=[None,'_media'])
        if incl == 'places':
            df_incl = df_incl.drop_duplicates(subset=['id'])
            df_tweets = pd.merge(df_tweets, df_incl, how='left', left_on=['place_id'], right_on=['id'],
                                 suffixes=[None,'_places'])
        if incl == 'users':
            df_incl = df_incl.drop_duplicates(subset=['id'])
            df_tweets = pd.merge(df_tweets, df_incl, how='left', left_on=['author_id'], right_on=['id'],
                                 suffixes=[None,'_users'])

        if incl == 'tweets':
            # extract nested referenced_tweet id
            df_tweets['referenced_tweet_lst'] = df_tweets['referenced_tweets'].\
                apply(lambda x: x[0] if type(x) == list else {})

            df_ref = pd.DataFrame(df_tweets['referenced_tweet_lst'].to_dict()).T
            df_ref.columns = ['referenced_tweet_type', 'referenced_tweet_id']
            df_tweets = pd.concat([df_tweets.drop(['referenced_tweet_lst'], axis=1), df_ref], axis=1)

            df_incl = df_incl.drop_duplicates(subset=['id'])
            df_tweets = pd.merge(df_tweets, df_incl, how='left', left_on=['referenced_tweet_id'],
                                 right_on=['id'], suffixes=[None, '_ref_tweet'])

    return df_tweets


def flat_dict(df):
    """
        Add each key-value of a nested dictionary that is saved in a dataframe, as a new column
    """
    for col in df.columns:
        if type(df[col][0]) == dict:
            df = pd.concat(
                [df.drop([col], axis=1), df[col].apply(pd.Series)], axis=1)
            # sometimes a column is dropped but column 0 stays
            df = df.drop([0], axis=1, errors='ignore')
    return df


def save_list(chunklist, filename_prefix):
    """
        Save a list of chunks with a given file-name prefix in parallel
    """
    argslist = ((chk, filename_prefix, i) for i, chk in enumerate(chunklist))

    cpu_no = psutil.cpu_count(logical = False)
    print('Number of available cpu cores',cpu_no)
    pool = Pool(cpu_no)  # run cpu_no tasks at most in parallel
    pool.map(save_chunk, argslist)
    print('Done')
