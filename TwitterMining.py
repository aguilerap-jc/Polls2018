import os
import sys 
import json
from pprint import pprint

class variables:
	CONSUMER_SECRET_KEY = "ConsumerSecretKey"
	CONSUMER_KEY 		= "ConsumerKey"
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

	def getConsumerKey(self,webpage):
		try:
			return json.load(open(self.JsonKeysFile))[self.var.CONSUMER_KEY][webpage]
		except:
			print("Required Web Keys arent available please try with a different webpage")
		
	def getConsumerSecretKey(self,webpage):
		try:
			return json.load(open(self.JsonKeysFile))[self.var.CONSUMER_SECRET_KEY][webpage]
		except:
			print("Required Web Secret Keys arent available please try with a different webpage")
		
	def getConsumerKeys(self):
		return json.load(open(self.JsonKeysFile))[self.var.CONSUMER_KEY]

	def getConsumerSecretKeys(self):
		return json.load(open(self.JsonKeysFile))[self.var.CONSUMER_SECRET_KEY]

	def getAllKeys(self):
		return json.load(open(self.JsonKeysFile))

	def getKeys(self,webpage):
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

class manageFiles:

	def getDirectory(self,directory):
		print("GetDir")
	
	def getFiles(self,path):
		print("GetFiles")
	
	def saveFiles(self,path):
		print("SaveFiles")

	def saveDirectory(self,path):
		print("Save Dir")

def main():
	var = variables()
	sa  = securityAdmin()


if __name__ == '__main__':
	main()