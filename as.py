import time
import struct

def lastbit(f):
	return struct.pack('!f', f)[-1] & 1

def getrandbits(k):
	result = 0
	for _ in range(k):
		time.sleep(0)
		result <<= 1
		result |= lastbit(time.clock())
	return result

def rand(a, b):
	return a + randbelow(b - a + 1)

def randbelow(n):
	if n <= 0:
		raise ValueError
	k = n.bit_length()
	r = getrandbits(k)
	while r >= n: # avoid skew
		r = getrandbits(k)
	return r

def bias(start, end, n):
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


ls = bias(1, 10, 100)
print(ls)




