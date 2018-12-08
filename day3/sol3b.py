import sys
from collections import defaultdict

lines = []
for line in sys.stdin:
    lines.append(line.strip())

claimed = defaultdict(list)
claims = {}
for line in lines:
    parts = line.split(' ')
    claim_id = int(parts[0][1:])
    corner = parts[2][:-1].split(',')
    size = parts[3].split('x')
    left_edge = int(corner[0])
    top_edge = int(corner[1])
    width = int(size[0])
    height = int(size[1])
    claims[claim_id] = (left_edge, top_edge, width, height)

    for x in range(left_edge, left_edge + width):
        for y in range(top_edge, top_edge + height):
            claimed[(x,y)].append(claim_id)

total = 0
for k,v in claimed.iteritems():
    if len(v) == 1:
        claim = v[0]
        left_edge, top_edge, width, height = claims[claim]
        valid = True
        for x in range(left_edge, left_edge + width):
            for y in range(top_edge, top_edge + height):
                if len(claimed[(x,y)]) > 1:
                    valid = False
        if valid:
            print claim



print total

