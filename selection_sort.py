import random
import math
import time

def insertion_sort(A):
    n = len(A)
    for i in range(0, n-1):
        smallest = i
        for j in range(i+1, n):
	    if A[j] < A[smallest]:
	       smallest = j
	if smallest != i:
	    A[smallest], A[i] = A[i], A[smallest]

a = []
for i in range(1, 1001):
    a.append(int(random.random()*10001))

begin = time.time()
insertion_sort(a)
end = time.time()

print a
print "It took %.2f seconds" % (end - begin)
