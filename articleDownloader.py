import os
import commands
from sets import Set
from BeautifulSoup import BeautifulSoup

wikiStart = "http://en.wikipedia.org"

def download(link, dest):
	if not os.path.exists(dest):
		commands.getoutput('wget "' + link + '" -O "' + dest+ '"')
		print "down", link

count = 0

while 1:
	try:
		count += 1
		print count
		x = raw_input().strip()
		if x.count("Done") > 0 : continue
		if not os.path.exists("./artsList/"+x+"Articles.txt") : continue
		f = open ("./artsList/"+x+"Articles.txt")
		content = [x[0:-1].split(" ")[0].replace('"',"") for x in  f.readlines()]
		for line in content:
			if line.count('Talk:'):continue
			if line.count('User:'):continue
			if line.count('Template:'):continue
			path = wikiStart + line
			if path.count('.svg') > 0 or path.count('.png') > 0 or path.count('.SVG') > 0 \
			or path.count('.PNG') > 0 or path.count('.jpg') > 0 or path.count('.JPG') > 0 \
			or path.count('.jpeg')> 0 or path.count('.JPEG')> 0:continue
			try:
				download(path, "./articles/"+path.replace(wikiStart,"").replace('/wiki/',''))
			except Exception as e:
				print e
				print "Error", x
				continue
	except EOFError:break 
