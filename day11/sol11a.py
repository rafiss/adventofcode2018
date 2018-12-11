import sys
from collections import Counter

serial_num = 5719

def compute_power(x, y):
    rack_id = x+ 10
    pwr = rack_id * y
    pwr += serial_num
    pwr *= rack_id
    pwr = pwr / 100
    pwr = pwr % 10
    pwr -= 5
    return pwr

square_power = Counter()
for x in range(1, 300 + 1 - 3):
    for y in range(1, 300 + 1 -3):
        pwr = 0
        for x_i in range(x, x+3):
            for y_i in range(y, y+3):
                pwr += compute_power(x_i, y_i)
        square_power[(x,y)] = pwr

print square_power.most_common(1)
