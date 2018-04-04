import os
import sys 
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from pprint import pprint

class variables:
	CONSUMER_SECRET_KEY = "ConsumerSecretKey"
	CONSUMER_KEY 		= "ConsumerKey"
	ACCESS_TOKEN 		= "AccessToken"
	ACCESS_TOKEN_KEY	= "AccessTokenSecret"
	JSON_KEY_FILE		= "Keys.json"
	TWITTER 			= "Twitter"
	FB 					= "FaceBook"
	GPLUS				= "GooglePlus"
	GOOGLE 				= "Google"

class securityAdmin:
	var = variables()
	JsonKeysFile  = str(os.getcwd())+"\\" +var.JSON_KEY_FILE

	def printKeys(self):
		temp = self.getKeys(self.var.TWITTER)
		print("Twitter: " 		+ temp[0] + "\t" + temp[1] )
		temp = self.getKeys(self.var.FB)
		print("Face Book: " 		+ temp[0] + "\t" + temp[1] )
		temp = self.getKeys(self.var.GPLUS)
		print("Google Plus : " 	+ temp[0] + "\t" + temp[1] )
		temp = self.getKeys(self.var.GOOGLE)
		print("Google :	"		+ temp[0] + "\t" + temp[1] )

	def getConsumerKey(self,webpage,file=JsonKeysFile):
		try:
			return json.load(open(file))[self.var.CONSUMER_KEY][webpage]
		except:
			print("Required Web Keys arent available please try with a different webpage")
		
	def getConsumerSecretKey(self,webpage,file=JsonKeysFile):
		try:
			return json.load(open(file))[self.var.CONSUMER_SECRET_KEY][webpage]
		except:
			print("Required Web Secret Keys arent available please try with a different webpage")
		
	def getConsumerKeys(self,file=JsonKeysFile):
		return json.load(open(file))[self.var.CONSUMER_KEY]

	def getConsumerSecretKeys(self,file=JsonKeysFile):
		return json.load(open(file))[self.var.CONSUMER_SECRET_KEY]

	def getAllKeys(self,file=JsonKeysFile):
		return json.load(open(file))

	def getAccessToken(self,webpage,file=JsonKeysFile):
		try:
			return json.load(open(file))[self.var.ACCESS_TOKEN][webpage]
		except:
			print("Required Web Secret Keys arent available please try with a different webpage")

	def getAccessTokenSecret(self,webpage,file=JsonKeysFile):
		try:
			return json.load(open(file))[self.var.ACCESS_TOKEN_KEY][webpage]
		except:
			print("Required Web Secret Keys arent available please try with a different webpage")

	def getAccessTokens(self,file=JsonKeysFile):
		return json.load(open(file))[self.var.ACCESS_TOKEN]

	def getAccessTokenSecrets(self,file=JsonKeysFile):
		return json.load(open(file))[self.var.ACCESS_TOKEN_KEY]

	def getKeys(self,webpage):
		return [ self.getAllKeys()[self.CONSUMER_KEY][webpage] , self.getAllKeys()[self.CONSUMER_SECRET_KEY][webpage] ]
		'''
		if(webpage == self.var.TWITTER):
			return [ self.getAllKeys()[self.var.CONSUMER_KEY][self.var.TWITTER] , self.getAllKeys()[self.var.CONSUMER_SECRET_KEY][self.var.TWITTER] ]
		elif(webpage == self.var.FB):
			print("Not Generated Yet")
			return [ self.getAllKeys()[self.var.CONSUMER_KEY][self.var.FB] 		, self.getAllKeys()[self.var.CONSUMER_SECRET_KEY][self.var.FB] ]
		elif(webpage == self.var.GPLUS):
			print("Not Generated Yet")
			return [ self.getAllKeys()[self.var.CONSUMER_KEY][self.var.GPLUS] 	, self.getAllKeys()[self.var.CONSUMER_SECRET_KEY][self.var.GPLUS] ]
		elif(webpage == self.var.GOOGLE):
			print("Not Generated Yet")
			return [ self.getAllKeys()[self.var.CONSUMER_KEY][self.var.GOOGLE] 	, self.getAllKeys()[self.var.CONSUMER_SECRET_KEY][self.var.GOOGLE] ]
		'''

class manageFiles:

	def getDirectory(self,directory):
		print("GetDir")
	
	def getFiles(self,path):
		print("GetFiles")
	
	def saveFiles(self,path):
		print("SaveFiles")

	def saveDirectory(self,path):
		print("Save Dir")

class Twitter:
	var = variables()
	JsonKeysFile  = str(os.getcwd())+"\\" +var.JSON_KEY_FILE

	sa = securityAdmin()
	consumer_key 	= sa.getConsumerKey(var.TWITTER)
	consumer_secret = sa.getConsumerSecretKey(var.TWITTER)
	access_token 	= sa.getAccessToken(var.TWITTER)
	access_secret	= sa.getAccessTokenSecret(var.TWITTER)

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token,access_secret)

	api = tweepy.API(auth)

	def __init__(self,file=JsonKeysFile):
		self.consumer_key 		= self.sa.getConsumerKey(self.var.TWITTER,file)
		self.consumer_secret 	= self.sa.getConsumerSecretKey(self.var.TWITTER,file)
		self.access_token 		= self.sa.getAccessToken(self.var.TWITTER,file)
		self.access_secret 		= self.sa.getAccessTokenSecret(self.var.TWITTER,file)

		self.auth = OAuthHandler(self.consumer_key,self.consumer_secret)
		self.auth.set_access_token(self.access_token,self.access_secret)

		self.api = tweepy.API(self.auth)

	def getLastStatus(self,amount=1,json=0):
		stat = []
		try:
			for status in tweepy.Cursor(self.api.home_timeline).items(amount):
				if json :
					stat.append(status._json)
				else:
					stat.append(status.text)
			return stat
		except:
			print("Amount of entries exceeded")

	def getFriends(self,json=1):
		frnds = []
		try:
			for friend in tweepy.Cursor(self.api.friends).items():
				if json :
					frnds.append(friend._json)
				else:
					frnds.append(friend.txt)
			return frnds 
		except:
			print("Amount of entries exceeded")

	def getMyTweets(self,json=1):
		tweets = []
		try:
			for tweet in tweepy.Cursor(self.api.user_timeline).items():
				if json :
					tweets.append(tweet._json)
				else:
					tweets.append(tweet.txt)
			return tweets 
		except:
			print("Amount of entries exceeded")		

class TwitterStreaming:
	var = variables()
	JsonKeysFile  = str(os.getcwd())+"\\" +var.JSON_KEY_FILE

	sa = securityAdmin()
	consumer_key 	= sa.getConsumerKey(var.TWITTER)
	consumer_secret = sa.getConsumerSecretKey(var.TWITTER)
	access_token 	= sa.getAccessToken(var.TWITTER)
	access_secret	= sa.getAccessTokenSecret(var.TWITTER)

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token,access_secret)

	api = tweepy.API(auth)

	def __init__(self,file=JsonKeysFile):
		self.consumer_key 		= self.sa.getConsumerKey(self.var.TWITTER,file)
		self.consumer_secret 	= self.sa.getConsumerSecretKey(self.var.TWITTER,file)
		self.access_token 		= self.sa.getAccessToken(self.var.TWITTER,file)
		self.access_secret 		= self.sa.getAccessTokenSecret(self.var.TWITTER,file)

		self.auth = OAuthHandler(self.consumer_key,self.consumer_secret)
		self.auth.set_access_token(self.access_token,self.access_secret)

		self.api = tweepy.API(self.auth)

	def start_listener(self,filt="#python"):
		twitter_stream = Stream(self.auth, TwitterListener() )
		twitter_stream.filter(track=[filt])

	def start_am_listener(self):
		twitter_stream = Stream(self.auth, TwitterListenerAM() )
		twitter_stream.filter(track=["#AMLO"])

	def start_ra_listener(self):
		twitter_stream = Stream(self.auth, TwitterListenerAM() )
		twitter_stream.filter(track=["#RicardoAnaya"])

	def start_mz_listener(self):
		twitter_stream = Stream(self.auth, TwitterListenerAM() )
		twitter_stream.filter(track=["#MargaritaZavala"])

	def start_jm_listener(self):
		twitter_stream = Stream(self.auth, TwitterListenerAM() )
		twitter_stream.filter(track=["#JoseMeade"])


class TwitterListener(StreamListener):
	def on_data(self,data):
		try:
			with open("twitter_general.json",'a') as f:
				f.write(data)
				return True 
		except BaseException as e:
			print("Error on_data: %s" %str(e))
		return True

	def on_error(self,status):
		print(status)
		return True 	

class TwitterListenerAM(StreamListener):
	def on_data(self,data):
		try:
			#fileName = filt+".json"
			with open("am.json",'a') as f:
				f.write(data)
				return True 
		except BaseException as e:
			print("Error on_data: %s" %str(e))
		return True

	def on_error(self,status):
		print(status)
		return True 	

class TwitterListenerRA(StreamListener):
	def on_data(self,data):
		try:
			#fileName = filt+".json"
			with open("RA.json",'a') as f:
				f.write(data)
				return True 
		except BaseException as e:
			print("Error on_data: %s" %str(e))
		return True

	def on_error(self,status):
		print(status)
		return True 	


class TwitterListenerMZ(StreamListener):
	def on_data(self,data):
		try:
			#fileName = filt+".json"
			with open("MZ.json",'a') as f:
				f.write(data)
				return True 
		except BaseException as e:
			print("Error on_data: %s" %str(e))
		return True


	def on_error(self,status):
		print(status)
		return True 	

class TwitterListenerJM(StreamListener):
	def on_data(self,data):
		try:
			#fileName = filt+".json"
			with open("JM.json",'a') as f:
				f.write(data)
				return True 
		except BaseException as e:
			print("Error on_data: %s" %str(e))
		return True

	def on_error(self,status):
		print(status)
		return True 	



def main():
	var = variables()
	sa  = securityAdmin()
	tw  = Twitter()
	tw_stream_am = TwitterStreaming()
	tw_stream_ra = TwitterStreaming()
	tw_stream_mz = TwitterStreaming()
	tw_stream_jm = TwitterStreaming()
	
	#tw_streaming.start_listener()
	tw_stream_am.start_am_listener()
	tw_stream_ra.start_ra_listener()
	tw_stream_mz.start_mz_listener()
	tw_stream_jm.start_jm_listener()


	'''
	for s in stat:
		print(s)
		print("\n\n")
	'''
	
if __name__ == '__main__':
	main()