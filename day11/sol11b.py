import sys
from collections import Counter
from itertools import product

serial_num = 5719

def compute_power(x, y):
    rack_id = x+ 10
    pwr = rack_id * y
    pwr += serial_num
    pwr *= rack_id
    pwr = pwr / 100
    pwr = pwr % 10
    pwr -= 5
    return pwr

grid = {(x,y):compute_power(x,y) for x,y in product(range(1, 301), range(1,301))}

best = {}
for x in range(1, 301):
    best[(x, 300)] = (grid[(x, 300)], 1)
for y in range(1, 301):
    best[(300, y)] = (grid[(300, y)], 1)


for x in range(299,0,-1):
    for y in range(299,0,-1):
        grown = best[(x+1, y+1)][0] + grid[(x,y)] + sum([grid[(x_i, y)] for x_i in range(x+1, 301)]) + sum([grid[(x,y_i)] for y_i in range(y+1,301)])
        if grown > grid[(x,y)]:
            best[(x,y)] = (grown, 1 + best[(x+1,y+1)][1])
        else:
            best[(x, y)] = (grid[(x,y)], 1)

largest = (0, 0, 0, 0)
for y in range(1, 301):
    for x in range(1, 301):
        best[(x, y)]
        cand = (x, y, best[(x,y)][1], best[(x,y)][0])
        if cand[3] > largest[3]:
            largest = cand
print largest

p = 0
for y in range(largest[1], largest[1] + largest[2]):
    for x in range(largest[0], largest[0] + largest[2]):
        p += grid[(x,y)]
for y in range(297, 301):
    for x in range(297, 301):
        print '{:2}  '.format(grid[(x,y)]),
    print
for y in range(297, 301):
    for x in range(297, 301):
        print x, y, best[(x,y)]
print 'brute'
for y in range(243, 246):
    for x in range(88, 92):
        for size in range(15, min(18, 2 + 300 - max(x,y))):
            pwr = 0
            for x_i in range(x, x+size):
                for y_i in range(y, y+size):
                    pwr += grid[(x_i, y_i)]
            print x, y, (pwr, size)


print p
