import random
import math
import time

def insertion_sort(A):
    n = len(A)
    count = 0
    for i in range(0, n-1):
        smallest = i
        for j in range(i+1, n):
	    count += 1
	    if A[j] < A[smallest]:
	       smallest = j
	if smallest != i:
	    A[smallest], A[i] = A[i], A[smallest]
    return count

def insertion_sort2(A):
    n = len(A)
    count = 0
    for i in range(0, n-1):
        smallest = i
	largest = n-i-1
        for j in range(i+1, n-i):
	    count += 1
	    if A[j] < A[smallest]:
	       smallest = j
	    if A[j] > A[largest]:
	       largest = j
	if smallest != i:
	    A[smallest], A[i] = A[i], A[smallest]
	if largest != n-i-1:
	    A[largest], A[n-i-1] = A[n-i-1], A[largest]
    return count

a = []
for i in range(1, 101):
    a.append(int(random.random()*10001))

begin = time.time()
count=insertion_sort(a)
end = time.time()
print "original selection sort;"
print a
print count, "if/else statement"
print "It took %.2f seconds" % (end - begin)

begin = time.time()
count=insertion_sort2(a)
end = time.time()
print "\nmodified selection sort:"
print a
print count, "if/else statement"
print "It took %.2f seconds" % (end - begin)
