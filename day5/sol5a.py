import sys

line = [line.strip() for line in sys.stdin][0]
ignored = set()

def reacts(x, y):
    if x.isupper() and y.islower():
        return x.lower() == y
    if y.isupper() and x.islower():
        return y.lower() == x
    return False

i = 0
while i < len(line) - 1:
    if i in ignored:
        i += 1
        continue

    if reacts(line[i], line[i+1]):
        ignored.add(i)
        ignored.add(i+1)
        left = i-1
        right = i+2
        while left >= 0 and right < len(line):
            if left in ignored:
                left -= 1
                continue
            if not reacts(line[left], line[right]):
                break
            ignored.add(left)
            ignored.add(right)
            left -= 1
            right += 1
    i += 1

print len(line) - len(ignored)
