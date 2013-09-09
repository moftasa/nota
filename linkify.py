# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:49:35 2013

@author: mostafa
"""

# from https://gist.github.com/guillaumepiot/4539986

import re

def auto_link(value):
    # Replace url to link
    urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="\1" target="_blank">\1</a>', value)
    # Replace email to mailto
    urls = re.compile(r"([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="mailto:\1">\1</a>', value)
    return value

def auto_link_simple(text):
    r = re.compile(r"(http://[^ ]+)")
    return r.sub(r'<a href="\1">\1</a>', text)
