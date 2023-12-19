from functools import reduce
import numpy as np
file = "input.txt"
#file = "sample.txt"

data = [line.strip() for line in open(file, 'r')]

mirrors = []
def find_mirror(line):
    # takes string and returns the position of all mirror points
    mirrors = []
    for n in range(1, len(line)):  # n denotes the index of the element to the right of ?mirror
        mirror = True
        step = 1
        while n - step > -1 and n - 1  + step < len(line):
            if line[n-step] != line[n - 1 + step]:
                mirror = False
                break
            step += 1
        if mirror == True:
            mirrors.append(n)
        n += 1
    return mirrors
def find_one_mirror(lines):
    mirrors = []
    for line in lines:
        mirrors.append(find_mirror(line))
    one_mirror = list(reduce(set.intersection, map(set, mirrors)))
    if len(one_mirror) == 0:
        #print("No vertical mirrors")
        return 0
    else:
        return one_mirror[0]



maps = [[]]
n = 0
for line in data:
    if line:
        maps[n].append(line)
    else:
        n += 1
        maps.append([])


horizontal_tally = 0
no_vertical_mirrors = []
for a_map in maps:
    if find_one_mirror(a_map):
        horizontal_tally += find_one_mirror(a_map)
    else:
        no_vertical_mirrors.append(a_map)
print(horizontal_tally)
print(len(maps))
print(len(no_vertical_mirrors))

for line in no_vertical_mirrors[0]:
    print(line)

print("----------------")
arr = [list(line) for line in no_vertical_mirrors[0]]
for line in arr:
    print(line)


arr = np.array(arr)
print("---------------")
arr = arr.transpose()
for line in arr:
    print(line)
print(find_one_mirror(arr))

verticalTally = 0
for a_map in no_vertical_mirrors:
    a_map = [list(line) for line in a_map]
    a_map = np.array(a_map)
    a_map = a_map.transpose()
    verticalTally += find_one_mirror(a_map)
print (verticalTally)
print (horizontal_tally)
print (horizontal_tally + 100* verticalTally)