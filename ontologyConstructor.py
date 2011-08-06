#!/usr/bin/python
import string
import re
# NER
f = open('./stump5')
lines = [x[0:-1] for x in f.readlines()]

def organization(item):
	keywords = ['administration', 'association','manufacturers']
	for i in range(len(keywords)):
		if item.count(keywords[i]) > 0: return 1
	return 0

def people(item):
	keywords = ['wicket-keeper','coach','selector','taker','curator','manager','people','centurion'\
	,'umpires','owner','captain','bowler','batsmen','commentators','players','cricketers',\
	'president','chairmen','secrataries','scorer']
	for i in range(len(keywords)):
		if item.count(keywords[i]) > 0: return 1
	return 0

def team(item):
	keywords = ['team','club','cricket_in']
	for i in range(len(keywords)):
		if item.count(keywords[i]) > 0: return 1
	return 0

def event(item):
	keywords = ['season','year','tour','competition','championship','world_cup','event','series','league']
	for i in range(len(keywords)):
		if item.count(keywords[i]) > 0: return 1
	return 0

def country(item):
	for i in range(len(countries)):
		if item.count(countries[i]) > 0: return 1
	return 0
	
def ground(item):
	keywords = ['ground','venue']
	for i in range(len(keywords)):
		if item.count(keywords[i]) > 0:return 1
	return 0
		
def history(item):
	keywords = ['history','century']
	for i in range(len(keywords)):
		if item.count(keywords[i]) > 0:return 1
	for i in range(len(years)):
		if item.count(years[i])> 0: return 1
	return 0

def getEntityType(item):
	item.replace('_the','')
	possibilities = []
	if item.count('stub'): return('USELESS')
	if item.count('article'): return('USELESS')
	if item.count('template'): return('USELESS')
	if item.count('_by_'):return getEntityType(item.split('_by_')[0])
	if item.count('_in_'):return getEntityType(item.split('_in_')[0])
	if item.count('_of_'):return getEntityType(item.split('_of_')[0])
	if event(item): possibilities.append('Event')
	if people(item):possibilities.append('Person')
	if team(item):possibilities.append('Team')
	if organization(item):possibilities.append('Organization')
	if country(item):possibilities.append('Country')
	if ground(item): possibilities.append('Ground')
	if history(item): possibilities.append('History')
	if len (possibilities) == 0:
		return 'Unknonwn'
	elif len(possibilities) == 1:
		return possibilities[0]

def NERTag(item, parent, parentType):
	entityType = getEntityType(string.lower(item))
	return entityType

stack = ['Base']
typeStack = ['Base']
oldLevel = -1
countries = [string.lower('_'.join(x.split()[1:]).strip()) for x in open('countries').readlines()]
years = [x[0:-1] for x in open('years').readlines()]
for line in lines:
	if line.count('Done'):continue
	level = line.count(' ')/4
	if level > oldLevel:
		stack.append(line.strip())
		typeStack.append( NERTag(line.strip(), stack, typeStack) )
	if level < oldLevel:
		stack.pop(-1)
		stack.pop(-1)
		stack.append(line.strip())
		typeStack.pop(-1)
		typeStack.pop(-1)
		typeStack.append( NERTag(line.strip(), stack, typeStack) )
	else:
		stack[-1] = line.strip()
		typeStack[-1] = NERTag(line.strip(), stack, typeStack)
	if typeStack[-1] in ['Event', 'Team', 'Country', 'Person', 'Ground']:
		print line, '['+ typeStack[-1] +']'
	oldLevel = level

