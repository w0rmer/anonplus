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

import libs.threadmanager
import libs.events
import libs.logs as logs

import libs.friends as friends
friends.load_friends()

import tunnels.directudp
tunnels.directudp.start()

try:
    while True:
        time.sleep(1)
except:
    libs.threadmanager.killall()
    print friends.save_friends()
