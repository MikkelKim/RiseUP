"""This module scrapes pictures from Twitter."""

import ntpath
import os
import sys
import urllib

import twitter


def read_from_filestream(fstream):
    """ Read.
    
    :param fstream: A file-like object.
    """
    return fstream.read()


def get_keys(filename='keys.txt'):
    """ Retrieve keys from given file.

    :param filename: A string representation of filename to read.
    """
    with open(filename, 'r') as f:
        keys = read_from_filestream(f).split('\n')

        CONSUMER_KEY = keys[0].split('=')[1]
        CONSUMER_SECRET = keys[1].split('=')[1]
        ACCESS_TOKEN = keys[2].split('=')[1]
        ACCESS_TOKEN_SECRET = keys[3].split('=')[1]

        key_pairs = dict(consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token_key=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET)
        return key_pairs


def get_twitter_api(key_pairs):
    """ Create and return Api class from twitter module.
    
    :param key_pairs: A dictionary that contains the following:
                        consmer_key, consumer_secret, access_token, access_token_secret.
    """
    api = twitter.Api(**key_pairs)
    return api


def main():
    key_pairs = get_keys()
    api = get_twitter_api(key_pairs)
    # TODO: Use click.
    args = sys.argv
    term_to_search = args[1]
    num_search = args[2]

    search_results = api.GetSearch(term=term_to_search, count=num_search)
    for status in search_results:
        if status.media:
            url = status.media[0]['media_url']
            if not os.path.exists('pictures'):
                os.mkdir('pictures')
            name = 'pictures/' + ntpath.basename(url)
            urllib.urlretrieve(url, name)


if __name__ == '__main__':
    main()
