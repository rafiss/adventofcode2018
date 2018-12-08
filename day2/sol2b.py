import sys

words = []
for line in sys.stdin:
    words.append(line.strip())

for w1 in words:
    for w2 in words:
        if len(w1) != len(w2):
            continue
        distance = 0
        to_remove = -1
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                to_remove = i
                distance += 1
                if distance > 1:
                    break
        if distance == 1:
            print w1, w2, w1[:to_remove] + w1[to_remove+1:]
