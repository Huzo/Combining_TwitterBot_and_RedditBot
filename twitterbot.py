import tweepy as tp 
import time 
import os 

#credentials 
consumer_key =''
consumer_secret = ''
access_token = ''
access_secret = ''

#log in
auth = tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)


while True:
	tweet_data = input("")
	time.sleep(5)
	try:
		if(len(tweet_data)>280):
			pass
		else:
			api.update_status(status=tweet_data)
			time.sleep(250)
	except Exception as e:
		print(e)
		pass


