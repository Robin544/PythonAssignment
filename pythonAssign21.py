# Let’s learn and practise concepts of API: (Taken more help from GOOGLE)

# Importing tweepy library to extract the tweets from Twitter.
import tweepy
import socket       # Socket will extract the IP Addresses of some common sites.
import spotipy      # Spotipy will play some music.

# QUESTION 1:
# What is an access token? Generate your access token for any API.(for example Twitter, Spotify etc).

with open("access-tokens.txt", 'r') as file:
    read_line = file.readlines()
print("\n", read_line)

# Reading Consumer key and secret from consumerKeys File.
consumerKey = "enter your consumer-key"
consumerSecret = "enter your consumer-secret"

# Authenticating twitter consumer key.
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.secure = True
authUrl = auth.get_authorization_url()

# Go to this url.
print("\nPlease Visit This link and authorize the app ==> ", authUrl)

# Writing access tokes to file
pin = input("\nEnter The Authorization PIN: ")
token = auth.get_access_token(verifier=pin)
accessTokenFile = open("accessTokens", "w")
accessTokenFile.write("Access Token: "+token[0]+'\n')
accessTokenFile.write("Access Token Secret: "+token[1]+'\n')
print("Now you can check your access token file.")


# QUESTION 2:
# Get the IP address of some common sites like Google, Facebook by using DNS lookup.

address1 = socket.gethostbyname('www.google.com')
address2 = socket.gethostbyname('www.facebook.com')
print("\n\nIP Address of google.com: %s\nIP Address of facebook.com: %s " % (address1, address2))


# QUESTION 3:
# Using Tweepy library try to extract tweets from Twitter.

print("\n\n")
consumer_key = "enter your consumer-key"
consumer_secret = "enter your consumer-secret"
access_key = "enter your access-token-key"
access_secret = "enter your access-token-secret"


# Function to extract tweets
def get_tweets(username):

    # Authorization to consumer key and consumer secret
    auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth1.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth1)

    # 180 tweets to be extracted
    # number_of_tweets = 180
    tweets = api.user_timeline(screen_name=username)

    # Empty Array
    tmp = []

    # Create array of tweet information: username, tweet id, date/time, text.
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created

    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)

    # Printing the tweets
    for i in tmp:
        print(i)


# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user whose tweets are to be extracted.
    get_tweets("@realDonaldTrump")


# QUESTION 4:
# What is a difference between library and API. Figure it out with examples.

with open("LIBRARYvsAPI.txt", 'r') as file:
    read_line1 = file.readlines()
print("\n\n", read_line1)


# QUESTION 5:
# Trying to access Spotify API. Find out some library for it and play some music.

# (There is an error occurred "NO token provided")

print("\n\n")
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify()

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


# Finally done.

print("\n\nDone")
