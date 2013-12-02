#!/usr/bin/python

import urllib
import re
import time
import urlparse
import cgi
import cgitb
cgitb.enable()

# POST
form   = cgi.FieldStorage()			# Get POST data
url  = form.getfirst("url")			#GET URL

#DOMINIO
domain = urlparse.urlparse(url).hostname

#HTML
html = urllib.urlopen(url).readlines()
html_js = urllib.urlopen(url).read()

#REGEX DOM 
patron = """(location\s*[\[.])|([.\[]\s*["']?\s*(arguments|dialogArguments|innerHTML|write(ln)?|open(Dialog)?|showModalDialog|cookie|URL|documentURI|baseURI|referrer|location|name|opener|parent|top|content|self|frames)\W)|(localStorage|sessionStorage|Database)"""
#REGEX JAVASCRIPTS
pattern = "(src|SRC)\ *=\ *['\"]?(.*\.js)([#?].*)?"


# HTML HEADERS
print "Content-Type: text/html; charset=UTF-8"	# Print headers
print ""

# HTML 

print '''
<html>
<head>
    <title>Dom King Kong - Beta - Dom Auditing T00l</title>
    <link href="files/style.css" media="screen" rel="stylesheet" type="text/css" />
	<script type="text/javascript" src="files/scripts/shCore.js"></script>
	<script type="text/javascript" src="files/scripts/shBrushJScript.js"></script>
	<link type="text/css" rel="stylesheet" href="files/shCoreDefault.css"/>
	<script type="text/javascript">SyntaxHighlighter.all();</script>
</head>
<body>'''

#Obtener Criticos
def criticos(patron,html):
	print "<h2 style=\"color:white\">Attack Vector:</h2> <br />"
	print "<textarea class=\"js\" style=\"margin: 2px; width: 906px; height: 506px;\">"
	d = 0;
	for line in html:
		d = d + 1
		if re.search(patron, line):
			print str(d) + ".- " + line
	print "</textarea><br />"

#Obtener JS
def jss(patron,html,dominio):
	print "<h2 style=\"color:white\">JSS:</h2> <br />"
	scripts = []
	matches = re.finditer(patron, html)
	for match in matches:
		script = match.group(2)
		if script not in scripts:
			scripts.append(script)
	#print "<textarea style=\"margin: 2px; width: 566px; height: 211px;\">"
	for script in scripts:
		print "[+] <a href=\"domkingkong.py?url=http://" + dominio + "/" + script + "\">JS</a><br />"

	#print "</textarea>"

#Obtener Codigo Fuente
def all_html(html):
	c = 0
	print "<h2 style=\"color:white\">Web Page Source Code</h2>"
	print "<textarea class=\"js\" style=\"margin: 2px; width: 906px; height: 506px;\">"	
	for linea in html:
		c = c + 1
		print str(c) + linea
	print "</textarea>"


criticos(patron,html)
all_html(html)
jss(pattern,html_js,domain)



print '''
</body>
</html>
'''
