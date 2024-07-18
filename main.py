import yfinance as yf
import tweepy

#Keys from Twitter API v2 and v1 - Read and Write Permissions 
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

#Create Tweepy Object
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

#Choose Symbols of Stock
symbols = ['aapl', 'goog', 'nvda', 'tsla', 'meta']

#Create the string to bve tweeted
tweet = ''

for symbol in symbols:
    current = yf.Ticker(symbol)
    price = current.info['currentPrice']
    curr_ou = symbol + ": $" + str(price)
    tweet += curr_ou + '\n'

#Post the tweet
client.create_tweet(text=tweet)
print("Posted")