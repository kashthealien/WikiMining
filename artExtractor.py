triggerStart = '<h2><a name="Pages_in_category" id="Pages_in_category"></a>Pages in category'
triggerStop = "<td></td></tr></table>"
printFlag = 0

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

while 1:
	try:
		x = raw_input().strip()
		if x.count("Done") > 0 : continue
		try:
			f = open("./categories/Category:"+x+".html")
			f2 = open("./artsList/"+x+"Articles.txt",'w')
			content = f.readlines()
			f.close()
			st = ""
			for x in content:
				if x.count(triggerStart) > 0:printFlag = 1
				elif printFlag == 1 and x.count(triggerStop) > 0: break
				elif printFlag:
					if x == "": continue
					if x[0:4] != "<ul>" and x[0:4] != "<li>": continue
					try:st += x.split('<a href=')[1].split(">")[0].replace("title=","") + '\n'				
					except:continue

			f2.write(st)
			f2.close()
		except:
			print "Error", x
			continue
	except EOFError:break
