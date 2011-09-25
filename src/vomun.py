#! /usr/bin/env python
VERSION = 'v0.0.0b0pre'
BUILD = 0
print('''
======================
= Anon+ %s
= Build: %s
======================
''' % (VERSION, BUILD))

import time

import libs.events
import libs.logs

import libs.friends as friends
friends.load_friends()

import tunnels.directudp
tunnels.directudp.start()

try:
	while True:
	    time.sleep(1)
except:
	print "exiting"
	exit(0)