### #test_case = open ('test_case.txt', 'r')



import sys

test_case = open(sys.argv[1],'r')
lines = []

for test in test_case:
	 lines.append(test.strip())

numOfWords = int(lines[0])
lines.remove(lines[0])

lines.sort(key = len)
lines.reverse()

count = 0
for l in lines:
	if ( count < numOfWords):
		print (l)
		count += 1 
	else:
		break
