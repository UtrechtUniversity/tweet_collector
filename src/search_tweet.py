import argparse
import sys
from os import environ
from tweet_utils import *

# https://github.com/twitterdev/search-tweets-python/tree/v2
# https://pypi.org/project/searchtweets-v2/#description
from searchtweets import (ResultStream,
                          load_credentials,
                          merge_dicts,
                          read_config,
                          gen_params_from_config)

CREDENTIAL_YAML_KEY = "search_tweets_v2"


def parse_cmd_args():
    argparser = argparse.ArgumentParser()

    argparser.add_argument("--credential-file",
                           dest="credential_file",
                           default=None,
                           help=("Location of the yaml file used to hold "
                                 "your credentials."))

    argparser.add_argument("--env-overwrite",
                           dest="env_overwrite",
                           default=True,
                           help=("""Overwrite YAML-parsed credentials with
                                 any set environment variables. See API docs or
                                 readme for details."""))

    argparser.add_argument("--config-file",
                           dest="config_filename",
                           default=None,
                           help="""configuration file with all parameters.""")

    return argparser


def main():
    argparser = parse_cmd_args()
    args_dict = argparser.parse_args()
    if args_dict.config_filename:
        configfile_dict = read_config(args_dict.config_filename)
    else:
        configfile_dict = {}
        print('configfile_dict is empty', configfile_dict)
        sys.exit(1)
    filename_prefix = configfile_dict.get("filename_prefix") \
        if configfile_dict.get("filename_prefix") is not None else 'tweets'
    results_per_file = int(configfile_dict.get("results_per_file")) \
        if configfile_dict.get("results_per_file") is not None else 1000

    # check credentials : first environmental variables are checked
    bearer_token = environ["SEARCHTWEETS_BEARER_TOKEN"] if environ.get(
        "SEARCHTWEETS_BEARER_TOKEN") is not None else None
    endpoint = environ["SEARCHTWEETS_ENDPOINT"] if environ.get(
        "SEARCHTWEETS_ENDPOINT") is not None else None
    creds_dict = {}

    # if environmental variables are None, read from credential_file
    if (bearer_token is None) | (endpoint is None):
        print('no credential available among the environment variables')
        if args_dict.credential_file is not None:
            creds_dict = load_credentials(filename=args_dict.credential_file,
                                          yaml_key=CREDENTIAL_YAML_KEY,
                                          env_overwrite=args_dict.env_overwrite)
        else:
            print('credential_file is empty', creds_dict)
            sys.exit(1)
    else:
        creds_dict['bearer_token'] = bearer_token
        creds_dict['endpoint'] = endpoint

    # merge two credential and config dics
    def dict_filter(x): return {k: v for k, v in x.items() if v is not None}
    config_dict = merge_dicts(dict_filter(configfile_dict),
                              dict_filter(creds_dict))

    # Generate parameters for Twitter API and call it
    stream_params = gen_params_from_config(config_dict)
    rs = ResultStream(tweetify=False, **stream_params)
    stream = rs.stream()

    # makes chunks of tweets and save them in separate files, in parallel
    tweet_list = [tweet for tweet in stream]
    chunklist = list(chunks(tweet_list, results_per_file))
    save_list(chunklist, filename_prefix)


if __name__ == '__main__':
    main()
