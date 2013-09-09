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
<meta name="viewprot" content="width=device-width, initial-scale=1.0" />
<link rel="shortcut icon" href="/favicon.ico" type="image/vnd.microsoft.icon" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" type="text/css" href="css/bootstrap.css" />
<style>
	body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
	}
.content {
    margin: 0 auto;
    max-width: 768px;
</style>
<link rel="stylesheet" type="text/css" href="css/bootstrap-responsive.css" />
<link rel="stylesheet" type="text/css" href="static/reduced_style.css" />


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

<div class="navbar navbar-fixed-top navbar-inverse">
	<div class="navbar-inner">

		<div class="container">
			<button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            			<span class="icon-bar"></span>
            			<span class="icon-bar"></span>
            			<span class="icon-bar"></span>
			</button>

			<a href="#" class="brand">نوتة</a>

			<div class="nav-collapse collapse">
			<ul class="nav">
				<li><a href="%s">الرئيسية</a></li>
				<li><a href="#input">أنشئ نوتة جديدة</a></li>
				<li><a href="#share">أنشر</a></li>
			</ul>

		</div>
		</div>
	</div>
</div>

<div class="container">
""" % site_url

# The following is about the cool image not yet compatible with bootstrap CSS

    if img_url != None:
	 print """<div id="header-img">
<img class="header-img" src="%s"></img>
</div><div id="content-with-image">""" % img_url
    else:
	print '<div class="content">' 
    print "<p>%s</p>" % text.replace('\n', '<br />') # convert line breaks
    
def sharing(text, url, base_url, filename):
    print "<div class='well'>"
    if filename:
        print "<a href='%s' class='btn'>تنزيل النص</a>" % (base_url + "/raw/" + filename)
    else:
        pass
    print "<h3><a name='share'>أنشر:</a></h3>"    
    print """<div class="btn-group">
	<a class="btn" href="https://twitter.com/home/?status=%s+%s">غرّد على تويتر <img src="static/twitter.png" alt="غرد" width="20px" /></a>""" % (urlsafe_encode(text[0:93]),  urlsafe_encode(url)) 
    print """
	<a class="btn" href="http://www.facebook.com/sharer.php?u=%s&t=%s">شارك على فيسبوك <img src="static/facebook.png" alt="شارك على فيسبوك" width="18px"/></a>
</div>
""" % (url, text[0:200])
    print "<h4>عنوان الصفحة:</h3><pre class='text-right'>" + url + "</pre>"
    print "</div>"
    
def form(default_text,base_url):
    url = base_url + "/nota.py"
    print "<h2><a name='input' id='create'>أنشئ نوتة جديدة</a></h2>"
    print '<form name="textform" action="%s" method="post">' % url
    print '<textarea name="textcontent" class="textcontent" id="textcontent" cols="40" rows="10">'
    print default_text.rstrip()
    print '</textarea><br />'
    print """<div  class="form-actions">
                <input class="btn btn-primary btn-large" type="submit" value="أحفظ" />
                <input type='button' class='btn btn-large' value='أمسح رقعة الكتابة' onclick="clearTextArea()">
        </form>"""

def tail():
    print """&nbsp;
    </div>
    </div>
    </div>
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.js"></script>
    </body>
    </html>"""
