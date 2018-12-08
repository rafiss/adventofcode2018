import sys

line = [line.strip() for line in sys.stdin][0]

def reacts(x, y):
    if x.isupper() and y.islower():
        return x.lower() == y
    if y.isupper() and x.islower():
        return y.lower() == x
    return False

def final_len(poly, bad_type):
    ignored = set()
    poly = poly.replace(bad_type, '').replace(bad_type.upper(), '')
    #for x in range(len(poly)):
        #if poly[x].lower() == bad_type.lower():
            #ignored.add(x)
    i = 0
    while i < len(poly) - 1:
        #if poly[i].lower() == bad_type.lower():
            #ignored.add(i)
            #i += 1
            #continue
        if i in ignored:
            i += 1
            continue

        if reacts(poly[i], poly[i+1]):
            ignored.add(i)
            ignored.add(i+1)
            left = i-1
            right = i+2
            while left >= 0 and right < len(poly):
                #if poly[right].lower() == bad_type.lower():
                    #ignored.add(right)
                    #right += 1
                    #continue

                if left in ignored:
                    left -= 1
                    continue
                if not reacts(poly[left], poly[right]):
                    break
                ignored.add(left)
                ignored.add(right)
                left -= 1
                right += 1
        i += 1

    return len(poly) - len(ignored)

unique_types = set([a.lower() for a in line])
shortest = len(line)
for bad_type in unique_types:
    current = final_len(line, bad_type)
    print bad_type, current
    shortest = min(shortest, current)

print shortest
