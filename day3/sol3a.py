import sys
from collections import Counter

lines = []
for line in sys.stdin:
    lines.append(line.strip())

claims = Counter()
for line in lines:
    parts = line.split(' ')
    corner = parts[2][:-1].split(',')
    size = parts[3].split('x')
    left_edge = int(corner[0])
    top_edge = int(corner[1])
    width = int(size[0])
    height = int(size[1])

    for x in range(left_edge, left_edge + width):
        for y in range(top_edge, top_edge + height):
            claims[(x,y)] += 1

total = 0
for k,v in claims.iteritems():
    if v > 1:
        total += 1

print total

