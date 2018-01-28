TUSHAR BHATNAGAR
tusharbhatnagar13@gmail.com
9810991494

Function getrandombits(): 
#Return k random bits using a relative drift of two clocks.
# assume time.sleep() and time.clock() use different clocks

function randint(a, b):
#Returns a random integer in range [a, b], including both end points.

randbelow(n):
#Returns a random int in the range [0,n).  Raises ValueError if n<=0.

function bias():
ls = []
	n1 = int(n/100*73)
	# n1 and n2 are no. of random numbers to be generated above and below(below or equal) the half respectively.
	count1 = count2 = 0
	# count1 and count2 are no. of random integers that have been generated above and below(below or equal) half respectively
	n2 = n - n1
	for i in range(n):
		# if the number of random numbers generated above half(count1) is greater than n1, stop generating more random numbers that are more than half.
		if (count1 < n1) and (count2 < n2):
			if (rand(0,100) < 73):
				# generate a random number above half if (rand(0,100) < 73) i.e. 73% times generate number greater than half is selected and increment count1
				count1 += 1
				ls.append(rand((start+end)//2+1, end))
			else:
				# generate a random number less than half, if (rand(0,100) >= 73) and increment count2
				count2 += 1
				ls.append(rand(start, (start+end)//2))
		elif (count2 < n2):
				# if (count1 == n1) i.e. if maximum number of generated no.s above half is equal to n1, then only generate no.s smaller than or equal to half
				count2 += 1
				ls.append(rand(start, (start+end)//2))
		else:
				# else if (count2 == n2), generate no.s greated than half
				count1 += 1
				ls.append(rand((start+end)//2+1, end))
	print(count1, count2)
	return ls
