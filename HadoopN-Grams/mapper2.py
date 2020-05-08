import sys
import re

file=sys.stdin

for line in file:
  line=line.strip()
  word,count =line.split('\t',1)
  print("%s\t%s" % (word, count))
