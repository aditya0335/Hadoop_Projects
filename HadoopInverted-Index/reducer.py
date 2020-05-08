import sys
inverted_index = {}

for line in sys.stdin:
    line = line.strip()
    word,filename = line.split("\t")
    if word in inverted_index:
        if(filename in inverted_index[word]):
            pass
        else:
            inverted_index[word] = inverted_index[word] + ", " + filename
    else:
        inverted_index[word] = filename


for word in inverted_index:
    print("{}\t{}".format(word,inverted_index[word]))
