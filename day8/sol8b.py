import sys

class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata
    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        tot = 0
        for m in self.metadata:
            idx = m-1
            if idx >= len(self.children) or idx < 0:
                continue
            tot += self.children[idx].value()
        return tot

line = sys.stdin.readline().strip()
entries = [int(i) for i in line.split(' ')]

print entries[:10]

def parse_node(pos):
    n = Node([], [])
    num_children = entries[pos]
    num_metadata = entries[pos+1]
    pos += 2
    my_len = 2
    my_metadata = 0
    for i in range(num_children):
        child, child_len, child_metadata = parse_node(pos)
        n.children.append(child)
        my_len += child_len
        pos += child_len
        my_metadata += child_metadata
    for i in range(num_metadata):
        meta = entries[pos]
        n.metadata.append(meta)
        pos += 1
        my_len += 1
        my_metadata += meta
    return n, my_len, my_metadata

print parse_node(0)[0].value()
