import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin]

lines[0] = lines[0].split(' ')[2]
min_p = -700
max_p = 700

plants = defaultdict(lambda: '.')
for i in range(len(lines[0])):
    plants[i] = lines[0][i]

notes = {}
for line in lines[2:]:
    parts = line.split(' ')
    notes[parts[0]] = parts[2]

def get_neighbors(p):
    return plants[p-2] + plants[p-1] + plants[p] + plants[p+1] + plants[p+2]

def all_plants():
    st = ''
    for p in range(min_p, max_p):
        st += plants[p]
    return st

def compute(ps):
    s = 0
    for p,v in ps.iteritems():
        if v == '#':
            s += p
    return s

generations = {}
for gen in range(20001):
    if gen > 607 or all_plants()[-10] == '#':
        print gen, len(all_plants().replace('.', '')), compute(plants), all_plants()[-130:]
    generations[all_plants()] = gen
    new_plants = defaultdict(lambda: '.')
    for p in range(min_p, max_p):
        new_plants[p] = notes[get_neighbors(p)]
    plants = new_plants
    if all_plants() in generations:
        period_beg = generations[all_plants()]
        period_len = gen - period_beg
        print 'cycle!', period_beg, period_len, gen
        break

last_gen = 50000000000
print period_beg + ((last_gen - period_beg) % period_len)
last_plants = {}
for ps,g in generations.iteritems():
    if g == period_beg + ((last_gen - period_beg) % period_len):
        last_plants_s = ps
for p in range(-500, 500):
    last_plants[p] = last_plants_s[p + 500]


