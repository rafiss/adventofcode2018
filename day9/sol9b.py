import sys
from collections import Counter

num_players = 404
#max_marble = 25
max_marble = 71852 * 100
player_to_score = Counter()

def normalize_pos(pos):
    if pos < 0:
        return len(marbles) + pos
    if pos >= len(marbles):
        return pos - len(marbles)
    return pos

class Node:
    def __init__(self, val, nxt=None, prv=None):
        self.val = val
        self.nxt = nxt
        self.prv = prv

def rm_node(n):
    prv = n.prv
    nxt = n.nxt
    prv.nxt = nxt
    nxt.prv = prv
    return nxt

def add_node(val, prv, nxt):
    n = Node(val, nxt, prv)
    prv.nxt = n
    nxt.prv = n
    return n

def seven_before(n):
    for i in range(7):
        n = n.prv
    return n

def print_list(n):
    beg = n
    while True:
        print '{} '.format(n.val),
        n = n.nxt
        if n == beg:
            break

zero = Node(0)
zero.nxt = zero
zero.prv = zero
one = add_node(1, zero, zero)
two = add_node(2, zero, one)

current_marble_node = two
current_player = 2

for m in range(3, max_marble+1):
    if m % 2000 == 0:
        print 'marble {} of {}'.format(m, max_marble)
    if m % 23 == 0:
        player_to_score[current_player] += m
        node_to_score = seven_before(current_marble_node)
        player_to_score[current_player] += node_to_score.val
        current_marble_node = rm_node(node_to_score)
    else:
        current_marble_node = add_node(m, current_marble_node.nxt, current_marble_node.nxt.nxt)

    current_player += 1
    current_player = current_player % num_players

#print_list(zero)

print player_to_score.most_common(1)
