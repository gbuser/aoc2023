file = "input.txt"
#file = "sample.txt"
data = [line.split() for line in open(file, 'r')]
seeds = data.pop(0)
data.pop(0) # getting rid opf blank line
seeds = [int(x) for x in seeds[1:]]
maps = [] #maps is a list of dictionaries of the mapping data
for line in data:
    if line and line[0][0].isalpha():
        new_map = []
    elif line == []:
        maps.append(new_map.copy())
    else:
        new_map.append({'start': int(line[1]), 'end': int(line[1]) + int(line[2]), 'map_to': int(line[0])})
maps.append(new_map.copy()) #o/w one map short!
def next_mapping(seed, n):
    # takes a source, a map and maps to next
    for item in maps[n]:
        if seed in range(item['start'], item['end']):
            return (seed + item['map_to'] - item['start'])
    return seed

locations = []
for seed in seeds:
    for n in range(len(maps)):
        seed = next_mapping(seed, n)
    locations.append(seed)
print(locations)
print(min(locations))



