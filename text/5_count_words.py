import re

str = raw_input()

f = open(str,"r")

whole = f.read()

lst = re.split("[ \n]",whole)
lst = filter(lambda x : len(x) != 0, lst)

print len(lst)
