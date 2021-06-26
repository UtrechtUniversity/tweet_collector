import argparse
import json
import sys

from searchtweets import (ResultStream,
                          load_credentials,
                          merge_dicts,
                          read_config,
                          write_result_stream,
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

    #Todo: add csv option
    return argparser


def main():
    argparser = parse_cmd_args()
    args_dict = argparser.parse_args()

    #Todo store as environment variable and read it
    #Todo number of tweets per file does not work
    if args_dict.config_filename is not None:
        configfile_dict = read_config(args_dict.config_filename)
    else:
        configfile_dict = {}
        print('configfile_dict is empty',configfile_dict )
        sys.exit(1)


    creds_dict = load_credentials(filename=args_dict.credential_file,
                                  #account_type=args_dict["account_type"],
                                  yaml_key=CREDENTIAL_YAML_KEY,
                                  env_overwrite=args_dict.env_overwrite)

    dict_filter = lambda x: {k: v for k, v in x.items() if v is not None}

    config_dict = merge_dicts(dict_filter(configfile_dict),
                              dict_filter(creds_dict)) #,dict_filter(args_dict)


    stream_params = gen_params_from_config(config_dict)

    rs = ResultStream(tweetify=False, **stream_params)


    filename_prefix = config_dict.get("filename_prefix")
    with open(filename_prefix, 'a', encoding='utf-8') as f:
        for tweet in rs.stream():

            json.dump(tweet, f)
            f.write('\n')

if __name__ == '__main__':
    main()
