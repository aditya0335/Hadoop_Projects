import sys
import re

for line in sys.stdin:
    line = line.strip()

    words = line.split()

    for word in words:
        new_word = re.sub(r'[\W_]+','',word)
        if(len(new_word) >= 1):
            print('{}\t{}'.format(new_word,1))


