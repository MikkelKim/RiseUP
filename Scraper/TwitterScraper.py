import sys
import urllib
import ntpath
import twitter

keyFile = open('TwitterKeys.txt', 'r')
keys = keyFile.read().split('\n')

CONSUMER_KEY = keys[0].split('=')[1]
CONSUMER_SECRET = keys[1].split('=')[1]
ACCESS_TOKEN = keys[2].split('=')[1]
ACCESS_TOKEN_SECRET = keys[3].split('=')[1]

keyFile.close()

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

args = sys.argv
termToSearch = args[1]
numSearch = args[2]

searchResults = api.GetSearch(term=termToSearch, count=numSearch)
for status in searchResults:
	if status.media:
		url = status.media[0]['media_url']
		name = 'pictures/' + ntpath.basename(url)
		urllib.urlretrieve(url, name)

