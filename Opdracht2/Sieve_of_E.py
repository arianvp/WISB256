#! /bin/env python3
import sys
import time

def sieve(n):
    a = [False] * 2 + [True]* (n-1)
    for i in range(int(n**0.5 + 1.5)):
        if a[i]:
            for j in range(i*i,n+1,i):
                a[j] = False
    for i in range(n+1):
        if a[i]: yield i



n = int(sys.argv[1])
out = sys.argv[2]

t1 = time.perf_counter()
primes = sieve(n)
t2 = time.perf_counter()

print("--------------------------------------------")

length = 0
with open(out,"wt") as f:
    for i in sieve(n):
        f.write("{}\n".format(i))
        length+=1

print("Found {} Prime numbers smaller than {} in {} sec.".format(length,n,t2-t1))
