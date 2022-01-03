import sys
count = 1
flag = False
for line in sys.stdin:
	if flag:
		line = line.strip()
		words = line.split(',')
		print(words[1],words[20],sep='\t')
		count += 1
	flag = True
