import os

path = './Selected/Matches/'
path2 = './Selected/Players/'

line1a = '<owl:NamedIndividual rdf:about="&Ontology1302497646005;'
lineEnd = '">'
line2a = '<rdf:type rdf:resource="&Ontology1302497646005;'
end = '</owl:NamedIndividual>'

properties = []
propCode = '<owl:DatatypeProperty rdf:about="&Ontology1302497646005;'

def RDFify(content, mode, rdfType, rdfName):
	if mode == 1:
		print line1a + rdfName + lineEnd
		print line2a + rdfType + lineEnd
		for x in content[1:]:
			a = x.split(' | ')[0]
			b = x.split(' | ')[1]
			tag = a.replace(' - ','_').replace(' ','_')
			if not tag in properties: properties.append(tag)
			print '<'+tag+'>'+b+'</'+tag+'>'
		print end
		print
	elif mode == 2:
		print line1a + rdfName + lineEnd
		print line2a + rdfType.replace(' ','_') + lineEnd
		for x in content:
			a = x.split(' | ')[0]
			b = x.split(' | ')[1]
			tag = a.replace(' - ','_').replace(' ','_').replace(', ','_')
			print '<'+tag+'>'+b+'</'+tag+'>'
		print end
		print

for x in os.listdir(path2):
	fil = open(path2+x)
	content = [a.strip('\n') for a in fil.readlines()]
	RDFify (content, 1, path2.replace('./Selected','').replace('/',''),x)

for x in os.listdir(path):
	fil = open(path+x)
	content = [a.strip('\n') for a in fil.readlines()]
	li = []
	for a in content:
		if a == '':
			RDFify (li, 2, li[1].split(' | ')[1],x+'_'+li[0].split(' | ')[1])
			li = []
		else:
			li.append(a)

for prop in properties:
	print propCode + prop + lineEnd
