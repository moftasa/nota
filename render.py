# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:19:30 2013

@author: mostafa
"""
import urllib
import linkify
import myconfig
from extractimage import find_image

def urlsafe_encode(string):
    return urllib.quote(string.encode('utf8'),"")
    
def convert_urls(text):
    pass

def head(title, url=None):
    print "Content-type:text/html,charset=utf-8"
    if url:
        print "Refresh: 0; url=%s" % url
    else:
        print
    print """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ar" lang="ar" dir="rtl">

<head>
<title> نوتة | %s </title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="/favicon.ico" type="image/vnd.microsoft.icon" />
<link rel="stylesheet" type="text/css" href="static/style.css" />

<script language="JavaScript" type="text/javascript">
function clearTextArea() {
document.getElementById("textcontent").value = "";
}
</script>
    """ % title
    
def twitter_card(base_url, url, text_content):
    print """
<meta name="twitter:card" content="summary">
<meta name="twitter:url" content="%s%s">
<meta name="twitter:title" content="%s">
<meta name="twitter:description" content="%s">
<meta name="twitter:image" content="http://nota.cc/static/icon.png">
""" % (base_url, url, text_content[0:93], text_content[93:294]) #twitter cards need absolute url to icon

def close_head():
    print "</head>"
    
def body(text, url, base_url):
    img_url = find_image(text)
    text = linkify.auto_link(text) # make urls linkable
    site_url = base_url + "/nota.py"
    print """
	<body>
	<div class="navbar">
		<div class="navbar-inner">

			<div class="container">

				<a href="#" class="brand" title="العودة لأعلى الصفحة">نوتة</a>

				<ul class="nav">
					<li><a href="%s">الرئيسية</a></li>
					<li><a href="#input">أنشئ نوتة جديدة</a></li>
					<li><a href="#share">أنشر</a></li>
				</ul>

			</div>
		</div>
	</div>""" % site_url
    if img_url != None:
	 print """<div id="header-img">
<img class="header-img" src="%s">
</div><div class="main with-image"><div id="text-margin">""" % img_url
    else:
	print '<div class="main"><div id="text-margin">' 
    print "<p>%s</p>" % text.replace('\n', '<br />') # convert line breaks
    
def sharing(text, url, base_url, filename):
    print "<div id='sharing'>"
    if filename:
        print "<h3><a href='%s' class='social-link'>تنزيل النص</a></h3>" % (base_url + "/raw/" + filename)
    else:
        pass
    print "<h3>أنشر:</h3>"    
    print """
<a href="https://twitter.com/home/?status=%s+%s" title="غرّد" class="social-link"><img src="static/twitter.png" alt="غرد" /></a>
""" % (urlsafe_encode(text[0:93]),  urlsafe_encode(url)) 
    print """
<a title="شارك على فيسبوك" href="http://www.facebook.com/sharer.php?u=%s&t=%s" target="_blank" class="social-link">
<img src="static/facebook.png" alt="شارك على فيسبوك" />
</a>
""" % (url, text[0:200])
    print "<h3>عنوان الصفحة:</h3><pre>" + url + "</pre>"
    print "</div>"
    
def form(default_text,base_url):
    url = base_url + "/nota.py"
    print "<h2><a name='input' id='create'>أنشئ نوتة جديدة</a></h2>"
    print '<form name="textform" action="%s" method="post">' % url
    print '<textarea id="textcontent" name="textcontent" class="form-textarea" cols="40" rows="10">'
    print default_text.rstrip()
    print '</textarea><br />'
    print '<input id="edit-submit" type="submit" value="أحفظ" />'
    print '''<input type='button' id='edit-clear' value='أمسح رقعة الكتابة' onclick="clearTextArea()">'''
    print '</form>'

def tail():
    print '&nbsp;'
    print '</div>'
    print '</div>'
    print "</body>"
