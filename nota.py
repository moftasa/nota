#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat Apr  6 19:35:55 2013

@author: mostafa
"""
import cgi
import cgitb; cgitb.enable(display=1, logdir=None)

import render
import stripHTML
import filestore

from myconfig import *
#from localconfig import *

# temporary solution to utf8 problem
import codecs, sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
# If you need input too, read from char_stream as you would sys.stdin
char_stream = codecs.getreader('utf-8')(sys.stdin)

#Create instance of FieldStorage 
form = cgi.FieldStorage()

def landing_page():
    text_content = filestore.read(about)
    url = base_url 

    renderer(text_content, url)
     
def note_page_GET():
    #Input via GET requesting a specific note
    note = form.getvalue('note')
    text_content = filestore.read(note)
    url = base_url + "/" + note
    
    renderer(text_content, url, note)
    
def note_page_POST():
    #Input via POST
    text_content = form.getvalue('textcontent')
    text_content = text_content.decode("utf-8")
    text_content = text_content.rstrip()
   
    filename = filestore.write(text_content) # write data to disk
   
    url = base_url + "/" + filename
   
    redirect = True #changes url in the address bar to new note url
    renderer(text_content, url, filename, redirect)

def renderer(text_content, url, filename=None, redirect=None):
    #strip HTML
    text_content = stripHTML.strip_tags(text_content)
    
    title = text_content[0:99]
    if redirect:
        redirect = url
    
    render.head(title, redirect)
    render.twitter_card(base_url, url, text_content)
    render.close_head()
    render.body(text_content, url, base_url)
    render.sharing(text_content, url, base_url, filename)
    render.form(text_content, base_url)
    render.tail()
    

# Get data from fields
if form.getvalue('textcontent'):
   note_page_POST()
   
elif form.getvalue('note'):
    note_page_GET()
    
else:
   landing_page()
