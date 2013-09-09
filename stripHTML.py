# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:13:01 2013

@author: mostafa
"""

from xml.sax.saxutils import escape
# escape() takes care of &, < and >.
html_escape_table = {
    '"': "&quot;",
    "'": "&apos;"
}

def strip_tags(text):
    return escape(text, html_escape_table)
