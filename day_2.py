# Part 1
def is_consistent(levels):
    ascending = False
    descending = False

    for i in range(1, len(levels)):
        # check if the range between levels is greater than 3
        if abs(levels[i - 1] - levels[i]) > 3:
            return False
        if levels[i] > levels[i - 1]:
            ascending = True
        if levels[i] < levels[i - 1]:
            descending = True

    return not (ascending and descending)

def has_duplicates(levels):
    return len(levels) != len(set(levels))

with open('day-2-input.txt') as f:
    reports = f.readlines()
    safeTotal = 0

    for report in reports:
        levels = [int(level) for level in report.split(' ')]

        if is_consistent(levels) and not(has_duplicates(levels)):
            safeTotal += 1

    print(f"Safe total: {safeTotal}")
