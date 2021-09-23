"""Load data into Elasticsearch"""

import argparse
import json
import re
from pathlib import Path
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch.helpers import bulk


def document_generator(fp):
    """JSON lines doc generator."""
    if re.match('.*_[0-9].json', str(fp)):
        print(f'Load {Path(fp).name}...')
        with open(fp, "r") as f:
            for line in f:
                doc = json.loads(line)
                yield {
                    "_index": "twitter",
                    "_source": doc
                }
    else:
        print(f'Load all files named {Path(fp).stem}_x{Path(fp).suffix}...')
        files = list(Path(fp).parent.glob(
            f'{Path(fp).stem}*{Path(fp).suffix}'))
        for file in files:
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


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Load tweet file into ElasticSearch.'
    )
    parser.add_argument('--input_fp', type=str, help='source file')
    parser.add_argument('--mapping_fp',
                        type=str,
                        default= "mapping_twitter_tweet.json",
                        help='map file')
    args = parser.parse_args()

    # setup Elasticsearch client
    es = Elasticsearch()

    load_data_elasticsearch(es, args.input_fp, args.mapping_fp)
