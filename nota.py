# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 03:20:13 2013

@author: mostafa
"""

import web
from web import form
import filestore
import stripHTML
import linkify

render = web.template.render('templates/')

urls = (
    '/(.*)', 'Index',
    )
    
noteform = form.Form(
    form.Textarea('note', form.notnull, rows=10, cols=40, class_="form-textarea"))

class Index:
    def GET(self, nota):
        form = noteform()        
        nota, date = filestore.read(nota)
        return render.index(nota, form, date)
        
    def POST(self, nota):
        form = noteform()
        nota = web.input(id="note")['note']  # this is a hack, not proper way.
        
        nota = nota.strip()
        nota = stripHTML.strip_tags(nota)
        #nota = linkify.auto_link(nota)
        
        filename = filestore.write(nota)
        raise web.seeother('/' + filename)
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
