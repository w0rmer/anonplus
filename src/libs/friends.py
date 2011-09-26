'''This module loads a list of friends out of ~/.vomun/friends.json'''
import json
import os.path
from libs.logs import logger as log

friends = []
friendlist = None

def load_friends():
    global friends
    
    friendlistpath = os.path.expanduser("~/.vomun/friends.json")
    friendlist = open(friendlistpath,"rw")
    friendsjson = json.loads(friendlist.read())
    for friend in friendsjson:
        try:
            port = friend["port"]
            keyid = friend["keyid"]
            name = friend["keyid"]
            ip = friend["lastip"]
            friendo = Friend(ip, port, name, keyid)
            log.info(friendo) # TODO update log system and this usage
            
            friends.append(friendo) # Add to the friends list

        except Exception as ex: 
            print ex, friend

def save_friends():
    '''Save the list of friends'''
    pass

def add_friend(nodeid, address, port):
    '''Add a friend'''
    pass

def del_friend(nodeid):
    '''Delete a friend'''
    pass

class Friend:
    def __init__(self, ip, port=1337, name = "unknown", keyid= "00000000000"):
        self.ip = ip
        self.port = port
        self.name = name
        self.keyid = keyid
    def __str__(self):
        return "<friend %s on %s:%i with id %s>" % (
                self.name, self.ip, self.port, self.keyid)