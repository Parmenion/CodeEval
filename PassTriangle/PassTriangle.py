"""import sys

test_case = open ('test_case.txt', 'r')
#test_case = open(sys.argv[1],'r')

tree = []
result = 0
for test in test_case:
	test = test.strip()
	tree.append(test.split())

col = 0
for level in tree:
	if (level == tree[0]):
		result = int(level[0])
	else:
		if (level[col] > level[col+1]):
			result += int(level[col])
		else:
			result += int(level[col+1])


print (result)



"""

import sys

with open ('test_case.txt', 'r') as input:
    test_cases = input.read().strip().splitlines()

triangle = [[int(n) for n in l.split()] for l in test_cases if l]

for row in range(len(triangle) - 1, -1, -1):
    for number in range(len(triangle[row]) - 1):
        chosen = max(triangle[row][number] + triangle[row - 1][number],
                     triangle[row][number + 1] + triangle[row - 1][number])
        triangle[row - 1][number] = chosen

print (triangle[0][0])