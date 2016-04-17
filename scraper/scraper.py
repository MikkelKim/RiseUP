import ntpath
import os
import sys
import urllib

import twitter


key_file = open('keys.txt', 'r')
keys = key_file.read().split('\n')

CONSUMER_KEY = keys[0].split('=')[1]
CONSUMER_SECRET = keys[1].split('=')[1]
ACCESS_TOKEN = keys[2].split('=')[1]
ACCESS_TOKEN_SECRET = keys[3].split('=')[1]

key_file.close()

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

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
