import sys
import re

lines = [line.strip() for line in sys.stdin]

pts = []
vs = []
for line in lines:
    match = re.search('position=<(.+), (.+)> velocity=<(.+), (.+)>', line)
    pts.append((int(match.group(1)), int(match.group(2))))
    vs.append((int(match.group(3)), int(match.group(4))))

max_size = 100

def get_corners(ps):
    xs = [p[0] for p in ps]
    ys = [p[1] for p in ps]
    return min(xs), min(ys), max(xs), max(ys)

def print_pts(ps, xmin, xmax, ymin, ymax):
    pset = set(pts)
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if (x, y) in pset:
                print '*',
            else:
                print ' ',
        print
    print '\n'


print pts[:10]
for i in range(44033):
    xmin, ymin, xmax, ymax = get_corners(pts)
    if abs(ymax - ymin) < 15:
        print 'second {}'.format(i)
        print_pts(pts, xmin, xmax, ymin, ymax)
    pts = [(x+v_x, y+v_y) for ((x, y), (v_x, v_y)) in zip(pts, vs)]

print pts[:10]

