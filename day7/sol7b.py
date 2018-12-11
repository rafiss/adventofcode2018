import sys
from collections import defaultdict
import re

lines = [line.strip() for line in sys.stdin]

adj = defaultdict(set)
rev = defaultdict(set)
all_nodes = set()
next_nodes = set()
topo = []

for line in lines:
    match = re.search('Step (\S+) must be finished before step (\S+) can begin', line)
    frm = match.group(1)
    to = match.group(2)
    adj[frm].add(to)
    rev[to].add(frm)
    all_nodes.add(frm)
    all_nodes.add(to)

for n in all_nodes:
    if len(rev[n]) == 0:
        next_nodes.add(n)

while len(next_nodes) > 0:
    n = min(next_nodes)
    next_nodes.remove(n)
    topo.append(n)
    for m in adj[n]:
        #adj[n].remove(m)
        rev[m].remove(n)
        if len(rev[m]) == 0:
            next_nodes.add(m)

print ''.join(topo)
