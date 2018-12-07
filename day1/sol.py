f = open('input', 'r')
deltas = [int(line) for line in f.readlines()]
found = False
current = 0
seen = set()

while not found:
    for d in deltas:
        seen.add(current)
        current += d
        if current in seen:
            print current
            found = True
            break
