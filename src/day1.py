'''
https://adventofcode.com/2024/day/1
'''

from collections import defaultdict
li0 = []
li1 = []
with open('src/resources/day1/lists.txt', encoding='utf-8') as fp:
    for line in fp:
        li0.append(int(line.split()[0]))
        li1.append(int(line.split()[1]))


# part 1
li0.sort()
li1.sort()
running_sum = 0  # our difference score
for i, x in zip(li0, li1):
    running_sum += abs(x - i)

print(running_sum)


# part 2

value_count = defaultdict(lambda: 0)
similiarity_score = 0
for i in li1:
    value_count[i] += 1

for i in li0:
    similiarity_score += i * value_count[i]

print(similiarity_score)
