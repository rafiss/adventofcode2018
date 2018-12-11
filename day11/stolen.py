import collections
import re

"""
Trying solution by sophiebits from
https://www.reddit.com/r/adventofcode/comments/a53r6i/2018_day_11_solutions/ebjoinm/
"""

ser = 5719

grid = {}
for i in xrange(1, 301):
  for j in xrange(1, 301):
    rack_id = i + 10
    then = (rack_id * j + ser) * rack_id
    powr = ((then // 100) % 10) - 5
    grid[(i,j)] = powr


m = -100
mxy = 0
for i in xrange(1, 301):
  for j in xrange(1, 301):
    k = grid[(i, j)]
    if k > m:
      m = k
      mxy = (i, j)
print mxy


# sums[(x, y)] is the cumulative sum of grid[(i, j)] for all i <= x and j <= y
sums = {}
for i in xrange(1, 301):
  for j in xrange(1, 301):
    sums[(i, j)] = grid[(i, j)] + sums.get((i - 1, j), 0) + sums.get((i, j - 1), 0) - sums.get((i - 1, j - 1), 0)
max_pwr = -100
max_square = 0
for i in xrange(1, 301):
  for j in xrange(1, 301):
    for s in xrange(1, 301 - max(i, j)):
      current = sums[(i + s-1, j + s-1)] + sums.get((i-1, j-1), 0) - sums.get((i + s-1, j-1), 0) - sums.get((i-1, j + s-1), 0)
      if current > max_pwr:
        max_pwr = current
        max_square = (i, j, s)

print max_pwr, max_square
