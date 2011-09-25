'''This module loads a list of friends out of ~/.vomun/friends.json'''
import json
import os.path
from libs.logs import logger as log
friends = {}
friendlist = None
def load_friends():
    friendlistpath = os.path.expanduser("~/.vomun/friends.json")
    friendlist = open(friendlistpath,"rw")
    friendsjson = json.loads(friendlist.read())
    for fri in friendsjson:
    	try:
    		port = fri["port"]
    		keyid = fri["keyid"]
    		name = fri["keyid"]
    		ip = fri["lastip"]
    		friendo = friend(ip,port,name,keyid)
    		log.info(friendo)

    	except Exception as ex: 
    		print ex, fri

def save_friends():
    '''Save the list of friends'''
    pass

def add_friend(nodeid, address, port):
    '''Add a friend'''
    pass

def del_friend(nodeid):
    '''Delete a friend'''
    pass

class friend:
	def __init__(self,ip,port=1337,name = "unknown", keyid= "00000000000"):
		self.ip = ip
		self.port = port
		self.name = name
		self.keyid = keyid
	def __str__(self):
		return "<friend %s on %s:%i with id %s>"%(self.name,self.ip,self.port,self.keyid)