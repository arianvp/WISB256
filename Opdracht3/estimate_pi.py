import random
import sys

from math import sin, cos
import math

try:
    if len(sys.argv) > 3:
        s = int(sys.argv[3])
        random.seed(s)
    l = float(sys.argv[2])
    n = int(sys.argv[1])


    def drop_needle(l):
        x0 = random.random()
        phi = random.vonmisesvariate(0,0)

        x = x0 + l*cos(phi)

        start = min(x0,x)
        end = max(x0,x)

        if start <= 0:
            return end >= 0

        if start <= 1:
            return end >= 1


    hits = 0
    for i in range(0,n):
        if drop_needle(l):
            hits += 1

    p = float(hits) / float (n)
    pi = 0
    if l <= 1:
        pi = 2 * l * (1/p)
    if l > 1:
        pi = 2*(l - math.sqrt(l*l-1) - math.asin(1/l)) / (p-1)


    

    print("{} hits in {} tries".format(hits,n))
    print("Pi = {}".format(pi))
except:
    raise
    print("Use: estimate_py N L S")



