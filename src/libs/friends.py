'''This module loads a list of friends out of ~/.vomun/friends.json'''
import json
import os.path
friends = {}
friendlist = None
def load_friends():
    friendlistpath = os.path.expanduser("~/.vomun/friends.json")
    friendlist = open(friendlistpath,"rw")
    friends = json.loads(friendlist.read())

def save_friends():
    '''Save the list of friends'''
    pass

def add_friend(nodeid, address, port):
    '''Add a friend'''
    pass

def del_friend(nodeid):
    '''Delete a friend'''
    pass
