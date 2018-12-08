import sys
from collections import Counter

num3 = 0
num2 = 0

for line in sys.stdin:
    cntr = Counter()
    for c in line:
        cntr[c] += 1
    inv_map = {v: k for k, v in cntr.iteritems()}
    if 3 in inv_map:
        num3 += 1
    if 2 in inv_map:
        num2 += 1

print num3*num2
