import sys

current= None
current_cnt=0
word=None
count_matrix=[]

for line in sys.stdin:
  line=line.strip()
  word, count = line.split('\t',1)
  cnt=int(count)
  if current == word:
    current_cnt=current_cnt + cnt
  else:
    if current:
      count_matrix.append([current, current_cnt])
    current_cnt = cnt
    current = word

if current==word:
   count_matrix.append([current, current_cnt])

sorted_array= sorted(count_matrix, key=lambda x: x[1], reverse=True)

for i in range(0,10):
  print("%s\t%s" % (sorted_array[i][0], sorted_array[i][1]))
