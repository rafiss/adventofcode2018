import sys
from collections import Counter

num_players = 404
#max_marble = 25
max_marble = 71852
player_to_score = Counter()

marbles = [0, 2, 1]
current_marble_pos = 1
current_player = 2

def normalize_pos(pos):
    if pos < 0:
        return len(marbles) + pos
    if pos >= len(marbles):
        return pos - len(marbles)
    return pos

for m in range(3, max_marble+1):
    if m % 2000 == 0:
        print 'marble {} of {}'.format(m, max_marble)
    if m % 23 == 0:
        player_to_score[current_player] += m
        pos_to_score = normalize_pos(current_marble_pos - 7)
        if pos_to_score > len(marbles):
            print marbles, len(marbles)
            print m
            print pos_to_score
            print current_marble_pos
            print current_player
            break
        player_to_score[current_player] += marbles[pos_to_score]
        marbles = marbles[:pos_to_score] + marbles[pos_to_score+1:]
        current_marble_pos = normalize_pos(pos_to_score)
    else:
        current_marble_pos = normalize_pos(current_marble_pos + 2)
        marbles = marbles[:current_marble_pos] + [m] + marbles[current_marble_pos:]

    current_player += 1
    current_player = current_player % num_players

#print marbles
print player_to_score.most_common(1)
