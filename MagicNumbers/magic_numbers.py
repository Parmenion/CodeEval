import sys
from collections import OrderedDict

test_case = open ('test.txt','r')


def foo():
	for test in test_case:
		test = test.strip() 
		if len(test) == len("".join(set(test))):
			 print check_numbers(test)
			 


def check_numbers(numbers):
	print "\nNew row: " + numbers 
	i = 0
	check_string = []
	for num in numbers: check_string.append(num)
	
	for n in numbers:
		print "\n" + str(i)
		x = i
		print "i before if = " + str(i) + "  numbers[i] = " + numbers[i] 
		if i + int(numbers[i])-1 >= len(numbers):
			o = int(numbers[i]) - len(numbers)
			if o > len(numbers):
				o = o/len(numbers)
			print "i = " + str(i)
			print "o = " + str(o)	
			i = int(numbers[i+o])
			print "numbers[i] = " + str(i)

		else:

			i = int(numbers[i])	
			print "Kortare an strangen: i = " + str(i) + " numbers[i] = " + numbers[i]

		print "kolla innan check_string: " + str(i)
		o = i
		print "x = " + str(x)
		if x + int(numbers[x]) >= len(numbers):
			o = int(numbers[x]) - len(numbers)
			if o > len(numbers):
				o = o/len(numbers)
			o = o+x
			print "ox = " + str(o)

		check_string[o] = 'x'
		print check_string
	return check_string


if __name__ == "__main__":
	foo()