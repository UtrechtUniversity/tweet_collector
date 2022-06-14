"""Load data into Elasticsearch"""
import argparse
import json
import re
import sys
from pathlib import Path
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch.helpers import bulk
from searchtweets import read_config

def document_generator(fp):
    """JSON lines doc generator."""
    print(f'Load all files named {Path(fp).stem}_x{Path(fp).suffix}...')
    files = list(Path(fp).parent.glob(f'{Path(fp).stem}*{".json"}'))
    for file in files:
        print(file)
        with open(file, "r") as f:
                for line in f:
                    doc = json.loads(line)
                    yield {
                        "_index": "twitter",
                        "_source": doc
                    }

def load_data_elasticsearch(es, fp, mapping_fp, verbose=False):
    """Create generator of file with tweets"""

    # create index and mapping if not exists
    if not es.indices.exists(index="index"):

        # mapping_fp = os.path.join("config", "mapping_twitter_tweet.json")
        with open(mapping_fp, "r") as f:
            mapping = f.read()

        es.indices.create(index='twitter', ignore=400, body=mapping)

    n, _ = bulk(es, document_generator(fp))
    print("Loaded {} files of tweet data into Elasticsearch".format(n))

    if verbose:
        print("The mapping of twitter:")
        print(es.indices.get_mapping(index='twitter'))

def main():
    parser = argparse.ArgumentParser(
        description='Load tweet file into ElasticSearch.'
    )
    parser.add_argument('--input_fp', type=str, help='source file', default='')
    parser.add_argument('--mapping_fp',
                        type=str,
                        default= "mapping_twitter_tweet.json",
                        help='map file')
    parser.add_argument("--config-file",
                           dest="config_filename",
                           default="config/api_config.config",
                           help="""configuration file with all parameters.""")

    args = parser.parse_args()


    configfile_dict = read_config(args.config_filename)


    '''upload data from filename_prefix in config file to elastic '''
    '''if filename_prefix is not provided, then upload data from input_fp'''
    fp=''
    if configfile_dict.get("filename_prefix") is not None:
        fp = configfile_dict.get("filename_prefix")+'.json'
    else:
        fp = args.input_fp

    if fp=='':
        print('No input file is provided')
        sys.exit(1)

    # setup Elasticsearch client
    es = Elasticsearch()

    load_data_elasticsearch(es, fp, args.mapping_fp)


if __name__ == '__main__':
    main()
