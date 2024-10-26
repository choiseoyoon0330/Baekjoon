from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input().strip())
tag_counts=defaultdict(int)

for _ in range(n):
    data = input().strip().split()
    tags = data[2:]
    for tag in tags:
        tag_counts[tag]+=1
    
max_count = max(tag_counts.values())
most_common_tags = [tag for tag, count in tag_counts.items() if count == max_count]
if len(most_common_tags) > 1:
    print(-1)
else:
    print(*most_common_tags)