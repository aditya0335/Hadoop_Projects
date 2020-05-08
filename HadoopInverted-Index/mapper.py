import sys
import os
import re

doc_tracker = {}
filenum = 0
for line in sys.stdin:
    line = line.strip()
    filepath = os.environ["map_input_file"]
    filename = filepath.split("/")[-1]

    words = line.split()

    for word in words:
        new_word = re.sub(r'[\W_]+','',word)
        if(len(new_word) >= 1):
            print("{}\t{}".format(new_word,filename))

