import os
import commands
from sets import Set
from BeautifulSoup import BeautifulSoup

testAttrs = ['','Dates |||| ','','Team1 |||| Score 1 A','','','','Team2 |||| Score 2 A','','Result |||| Loc, Count |||| Umpires |||| MOM '\
                    ,'','','Bat 1 A |||| Ball 1 A','','','','Bat 2 A |||| Ball 2 A','','','Score 1 B','','','','Score 2 B','','','Bat 1 B |||| Ball 2 B'\
                    ,'','','','Bat 2 B |||| Ball 2 B','','','Comments |||| ','']
ODIAttrs = ['', 'Date |||| ', '', 'Team1 |||| Score 1', '', '', '', 'Team 2 |||| Score 2', '', 'Result |||| Location |||| Umpires |||| MOM '\
                    , '', '', 'Bat 1 |||| Ball 1', '', '', '', 'Bat 2 |||| Ball 2', '', '', 'Comments |||| ', '']

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
            if os.path.exists("./matchInfoboxes/"+line.strip().replace('/wiki/','')+".txt"):continue
            st = ''            
            # Process the HTML
            try:
                mainSoup = BeautifulSoup(f)
                 # Find all match summary tables
                tables = mainSoup.findAll('table', {'style':"width: 100%; background-color: #EBF5FF"})
                
                # Go through each match in the page
                matchCount = 1
                for table in tables:
                    st += 'Match No | '+str(matchCount)+'\n'
                    matchCount += 1
                    
                    tableSoup = BeautifulSoup(str(table))
                    rows = tableSoup.findAll('tr')
                    if len(rows) == 5:
                        attrs = testAttrs            # Test Match attributes
                        st += 'Type | Test Match'
                    else:
                        attrs = ODIAttrs                                  # ODI attributes
                        st += 'Type | Limited Overs Match' +'\n'
                    values = []                                                     # Values for above attributes
                    
                    # Extraction part
                    for row in rows:
                        rowSoup = BeautifulSoup(str(row))
                        head = rowSoup.findAll('th')
                        ele = rowSoup.findAll('td')
                        numAttrs = len(head) + len(row)
                        li = head
                        li.extend(row)
                        for ele in li:
                            ele = str(ele).replace('<br>',' |||| ').replace('<br/>',' |||| ').replace('<br />',' |||| ')
                            ele = clean(ele)
                            clean(ele)
                            values.append(ele)

                    # Output part
                    for i in range(len(attrs)):
                        attr = attrs[i]
                        if attr == '': continue
                        if attr.count(' |||| '):
                            attrSplit = attr.split(' |||| ')
                            valSplit = values[i].split(' |||| ')
                            for j in range(len(attrSplit)):
                                if attrSplit[j] == '':continue
                                st +=  attrSplit[j] + ' | ' + valSplit[j] + '\n'
                        else:
                            st += attr + ' | ' + values[i] + '\n'
                    st += '\n'
            except Exception as e:
                print e  
            # Print results              
            try:
                f = open ("./matchInfoboxes/"+line.strip().replace('/wiki/','')+".txt",'w')
                f.write(st)
                f.close()
            except:
                print "Can't write file error"
    except EOFError:break 
