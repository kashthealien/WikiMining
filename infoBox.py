import os
import commands
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

count = 0
while 1:
    try:
        print count
        count += 1
        x = raw_input().strip()
        if x.count("Done") > 0 : continue
        if not os.path.exists("./artsList/"+x+"Articles.txt") : continue
        f = open ("./artsList/"+x+"Articles.txt")
        content = [x[0:-1].split(" ")[0].replace('"',"") for x in  f.readlines()]
        for line in content:
            # Try and open the required file
            try:
                f = open("./articles/"+line.strip().replace('/wiki/',''))
            except:    
                print "article not found error"
                continue
            # Skip if done
            if os.path.exists("./infoboxes/"+line.strip().replace('/wiki/','')+".txt"):continue
            st = ''
            
            # Process the HTML
            try:
                mainSoup = BeautifulSoup(f)
                tables = mainSoup.findAll('table')            # Find all tables
                for table in tables:
                    if len(table.attrs) > 0 and table.attrs[0][1].count('infobox'):    # Find the infobox table
                        tableSoup = BeautifulSoup(str(table))
                        rows = tableSoup.findAll('tr')
                        prevNumAttrs = 0
                        buff = []
                        for row in rows:
                            rowSoup = BeautifulSoup(str(row))
                            head = rowSoup.findAll('th')
                            row = rowSoup.findAll('td')
                            numAttrs = len(head) + len(row)
                            # If attr value pairs found, report
                            if numAttrs == 2:        
                                for h in head:
                                    st += clean(str(h)) + ' | '
                                for r in row:
                                    st += clean(str(r)) + ' | '
                                st += '\n'
                                buff = []
                            # Matrix mode
                            elif numAttrs > 2 and prevNumAttrs != numAttrs:
                                buff.append(head.extend(row))
                            else:
                                print "Matrix found"
                                print buff
                                buff = [head.extend(row)]
                            prevNumAttrs = numAttrs
                        if prevNumAttrs    > 2:
                            print "Matrix found"
                            print buff
            except Exception as e:
                print e  
            # Print results              
            try:
                f = open ("./infoboxes/"+line.strip().replace('/wiki/','')+".txt",'w')
                f.write(st)
                f.close()
            except:
                print "Can't write file error"
    except EOFError:break 
