def level(item):
    return item.count(' ')/4

li = []
done = []
allIn = []

while 1:
    try:
        inp = raw_input()
        if (inp.count('Done')): done.append(inp.replace('Done... ',''))
        else: li.append(inp)
        allIn.append(inp)
    except EOFError:break

a = []
for x in done:
    for i in range(len(li)):
        if x == li[i].strip():
            currLevel = level(li[i])
            i += 1
            a.append([])            
            while(level(li[i]) > currLevel):
                a[-1].append(li[i])
                i += 1
            break
   
for inp in allIn:
    if (inp.count('Done')):
        for x in a[0]: print x
        a.pop(0)        
    else:
        print inp

