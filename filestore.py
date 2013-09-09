# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:18:31 2013

@author: mostafa
"""
import random
import os
import codecs
import hashlib

path = 'raw/'

def random_characters(n):
    '''Create string of random characters of n size'''
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    list = random.sample(characters, n)
    return "".join(list)

def md5_hash(text):
     '''create md5 hex digest from text'''

     return hashlib.md5(text).hexdigest()
    
def write(text):
    #filename = random_characters(5)
    filename = md5_hash(text)
    if os.path.isfile(path + filename):
        #write(text)
	pass
    else:
        file = codecs.open(path + filename, "w", "utf8")
        file.write(text)
        file.close
    return filename
        
def read(filename):
    try:
        file = codecs.open(path + filename, "r", "utf8")
        text = file.read()
        file.close()
    except:
        text = "404 - الصفحة غير موجودة "
    return text
