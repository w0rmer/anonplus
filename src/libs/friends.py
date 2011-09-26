'''This module loads a list of friends out of ~/.vomun/friends.json'''
import json
import os.path
from libs.logs import logger as log

friends = {}
friendlistpath = os.path.expanduser("~/.vomun/friends.json")
friendlistr = open(friendlistpath,"r")


def load_friends():
    '''Load the List of friends'''
    friendsjson = json.loads(friendlistr.read())
    for friend in friendsjson:
        try:
            port = friend["port"]
            keyid = friend["keyid"]
            name = friend["keyid"]
            ip = friend["lastip"]
            friendo = Friend(ip, port, name, keyid)
            print friendo
            friends[keyid] = friendo
        except Exception as ex: 
            print ex, friend

def save_friends():
    friendlistw = open(friendlistpath,"w+")
    json = """[
%s
]"""
    friendsjson = ",".join([friend._json() for friend in friends.values()])

    friendlistw.write(json % friendsjson)

def add_friend(keyid, ip, port = 1337, name = "unknown"):
    '''Add a friend'''
    friendo = Friend(ip, port, name, keyid)
    friends[keyid] = friendo

def del_friend(keyid):
    '''Delete a friend'''
    try:
        del friends[keyid]
    except:
        log.info("could not delete friend %s: Friend not found" % keyid)

        
class Friend:
    def __init__(self, ip, port=1337, name = "unknown", keyid= "00000000000"):
        self.ip = ip
        self.port = port
        self.name = name
        self.keyid = keyid

    def _json(self):
        return """
    {
        "name": "%s",
        "keyid": "%s",
        "lastip": "%s",
        "port": %i    
    }""" % (self.name,self.keyid,self.ip,self.port)
    def __str__(self):
        return "<friend %s on %s:%i with id %s>" % (
                self.name, self.ip, self.port, self.keyid)