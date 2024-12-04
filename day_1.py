# Part 1
left_list = []
right_list = []

with open('day-1-input.txt') as f:
    lines = f.readlines()
    for line in lines:
        left, right = line.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))

left_list.sort()
right_list.sort()
total = 0

for i, j in zip(left_list, right_list):
    total += abs(i - j)
    
print(f"Part 1: {total}")

# Part 2
total = 0

for value in left_list:
    occurances = right_list.count(value)
    total += occurances * value

print(f"Part 2: {total}")