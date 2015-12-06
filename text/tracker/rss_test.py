import re
import urllib2

response = urllib2.urlopen("http://www.lidl.pl/pl/1974.htm")
page_source = response.read()

items = re.finditer("<h2 class=\"fn\">",page_source)
names = []

for match in items:
	start = match.span()[1]
	index = start 
	while page_source[index] != '<':
		index += 1
	names.append(page_source[start:index])

items2 = re.finditer("<span class=\"currency\">", page_source)
prices = []

for match in items2:
	end = match.span()[0]
	index = end
	while page_source[index] != '>':
		index -= 1
	prices.append(page_source[index+1:end])

print "size : " + str(len(prices))

whole = zip(names,prices)

for item in whole:
	print item[0] + " " + item[1]

