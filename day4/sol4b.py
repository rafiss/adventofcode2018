import sys
import re
from collections import Counter, defaultdict

lines = [line.strip() for line in sys.stdin]

guard_to_minutes = Counter()
guard_minute_to_times = defaultdict(Counter)
current_guard = 0
fell_asleep_at = 0

for line in lines:
    if 'begins' in line:
        match = re.search('#(\d+)', line)
        current_guard = int(match.group(1))
    if 'asleep' in line:
        match = re.search('00:(\d+)', line)
        fell_asleep_at = int(match.group(1))
    if 'wakes' in line:
        match = re.search('00:(\d+)', line)
        woke_up_at = int(match.group(1))
        guard_to_minutes[current_guard] += (woke_up_at - fell_asleep_at)
        for i in range(fell_asleep_at, woke_up_at):
            guard_minute_to_times[current_guard][i] += 1

best_guard = 0
best_minute = 0
best_times = 0
for guard, sleep_counter in guard_minute_to_times.iteritems():
    minute, total_times = sleep_counter.most_common(1)[0]
    if total_times > best_times:
        best_guard, best_minute = guard, minute
        best_times = total_times
    

print best_guard, best_minute, best_guard * best_minute
