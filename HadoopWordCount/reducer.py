import sys

word_count = {}

for line in sys.stdin:
    line = line.strip()
    word,count = line.split("\t")
    try:
        count = int(count)
    except:
        continue
    if(word in word_count):
        word_count[word]+=count
    else:
        word_count[word] = count

for word in word_count:
    print("{}\t{}".format(word,word_count[word]))
