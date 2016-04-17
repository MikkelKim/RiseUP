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

        consumer_key = keys[0].split('=')[1]
        consumer_secret = keys[1].split('=')[1]
        access_token = keys[2].split('=')[1]
        access_token_secret = keys[3].split('=')[1]

        key_pairs = dict(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_token_secret)
        return key_pairs


def get_twitter_api(key_pairs):
    """ Create and return Api class from twitter module.
    
    :param key_pairs: A dictionary that contains the following:
                        consmer_key, consumer_secret, access_token, access_token_secret.
    """
    api = twitter.Api(**key_pairs)
    return api


def analyze_status(status):
    """Dumb analyzer, just to prove concept.

    First of all, it needs to have `media`.
    Twitter status without pictures are useless for us.

    Some of interesting features we can extract:
        - checking geo coordinates
        - name from `place` content
        - keywords in hashtags
        - performing text analysis(NLP)
        - etc

    `place` has a set of coordinates under `bounding_box`. This could
    be the only thing we need.

    We should be able to come up with relatively simple models that 
    helps the scraper to decide if the picture is actually the picture.
    """
    # TODO: Lots of things todo here obviously.
    url = ''
    if status.media:
        url = status.media[0]['media_url']
    if status.geo:
        # If coordinates are within the range of a target, we gain certainty.
        pass
    if status.place:
        # If place is within the range of a target, we gain certainty.
        pass
    return url


def main():
    # Setups
    key_pairs = get_keys()
    api = get_twitter_api(key_pairs)
    if not os.path.exists('pictures'):
        os.mkdir('pictures')

    # TODO: Use click to grab arguments.
    args = sys.argv
    term_to_search = args[1]
    num_search = args[2]
    
    # Scrape.
    search_results = api.GetSearch(term=term_to_search, count=num_search)
    for status in search_results:
        url = analyze_status(status)
        if url:
            print 'Downloading {}'.format(url)
            name = 'pictures/' + ntpath.basename(url)
            urllib.urlretrieve(url, name)
    print 'Done.'


if __name__ == '__main__':
    main()
