# coding: utf-8
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#特定のユーザーのツイートを過去num件出力させる
def get_tweet(user, num):
	test = api.user_timeline(id = "%s"%user, count = num)
	for tweet in test:
		print(tweet.created_at)
		print(tweet.text)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#あるwordをnum件エゴサして出力させる
def search(word, num):
	keywords = [word]
	query = "OR".join(keywords)

	for tweet in api.search(q = query, num = kazu):
		print(tweet.created_at)
		print(tweet.user.screen_name)
		print(tweet.text)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

get_tweet("ここにUserID", 抽出するtweet数)

search("ここにエゴサするword", 抽出するtweet数)