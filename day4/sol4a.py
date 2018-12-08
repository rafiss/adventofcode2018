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

guard, total_minutes = guard_to_minutes.most_common(1)[0]
minute, total_times = guard_minute_to_times[guard].most_common(1)[0]

print guard, minute, guard * minute
