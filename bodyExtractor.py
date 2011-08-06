#!/usr/bin/python
import os
from sets import Set
from BeautifulSoup import BeautifulSoup

# Cleans a text by removing tags
def clean(in_text):
	s_list = list(in_text)
	i,j = 0,0
	while i < len(s_list):
		# iterate until a left-angle bracket is found
		if s_list[i] == '<':
			if s_list[i+1] == 'b' and s_list[i+2] == 'r' and s_list[i+3] == '>':
				i=i+1
				print hello
				continue				
			while s_list[i] != '>':
				# pop everything from the the left-angle bracket until the right-angle bracket
				s_list.pop(i)
			# pops the right-angle bracket, too
			s_list.pop(i)

		elif s_list[i] == '\n':
			s_list.pop(i)
		else:
			i=i+1
			
	# convert the list back into text
	join_char=''
	return (join_char.join(s_list))#.replace("<br>","\n")

# Writes the body to $product+Body.txt file
def getBody(product, dest):
	fil = "./"+product
	if not os.path.exists(fil):
		print "No file " + fil
		return
	myFile = open(fil)
	text = myFile.read().replace('\n',' ')
	mainSoup = BeautifulSoup(text)
	body = mainSoup.findAll('p')
	outStr = ""
	for x in body:
		outStr += clean(str(x)) + "\n"
	f = open(dest, 'w')
	f.write(outStr)
	f.close()

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
			fileName = "articles/"+line.strip().replace('/wiki/','')
			dest = "./articleBody/"+line.strip().replace('/wiki/','')
			if os.path.exists(dest): continue
			try:
				f = open(dest, 'w')
				f.write('')
				f.close()
			except:
				a = 1
			try:
				getBody(fileName, dest)
			except:
				print "Error: " + fileName
	except EOFError:break  
