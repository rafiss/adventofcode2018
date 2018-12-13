import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin]

lines[0] = lines[0].split(' ')[2]

plants = defaultdict(lambda: '.')
for i in range(len(lines[0])):
    plants[i] = lines[0][i]

notes = {}
for line in lines[2:]:
    parts = line.split(' ')
    notes[parts[0]] = parts[2]

def get_neighbors(p):
    return plants[p-2] + plants[p-1] + plants[p] + plants[p+1] + plants[p+2]

for gen in range(20):
    new_plants = defaultdict(lambda: '.')
    for p in range(-100, 200):
        new_plants[p] = notes[get_neighbors(p)]
    plants = new_plants

s = 0
for p,v in plants.iteritems():
    if v == '#':
        s += p
print s
