import sys
import re
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

file=sys.stdin
lemmatizer=WordNetLemmatizer()

for line in file:
  line=line.strip()
  line=re.sub('[^A-Za-z ]+','',line)
  line=re.sub('[A-Z]+', lambda m: m.group(0).lower(), line)
  words=line.split()
  for i,word in enumerate(words):
      word=lemmatizer.lemmatize(word)
      if(word=='science' or word=='sea' or word=='fire'):
        if((i-2)>-1):
          tri_word=words[i-2] + '_' + words[i-1] + '_' + '$'
          print("%s\t%s" % (tri_word,1))
        if((i-1)>-1 and (i+1)<len(words)):
          tri_word=words[i-1] + '_' + '$' + '_' + words[i+1]
          print("%s\t%s" % (tri_word,1))
        if(i+2<len(words)):
          tri_word='$' + '_' + words[i+1] + '_' + words[i+2]
          print("%s\t%s" % (tri_word,1))
