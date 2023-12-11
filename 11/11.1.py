import itertools
data = [line.strip() for line in open("input.txt", 'r')]
#data = [line.strip() for line in open("sample.txt", 'r')]
empty_rows = []
for row, values in enumerate(data):
    if '#' not in values:
        empty_rows.append(row)
empty_rows.sort(reverse= True)
print(empty_rows)
empty_cols = []
cols = {n : [] for n in range(len(data[0]))}
for line in data:
    for key, value in enumerate(line):
        cols[key].append(value)
for key in cols:
    if '#' not in cols[key]:
        empty_cols.append(key)
empty_cols.sort(reverse=True)
print(empty_cols)
blank_row = '.'*140
for row in empty_rows:
    data.insert(row, blank_row)

data = [list(row) for row in data]
for col in empty_cols:
    for row in data:
        row.insert(col, '.')
#the universe is expanded- wrong!needs to be simultaneous. try bottom to top and right to left
galaxies = []
for row_index, row in enumerate(data):
    for col_index, char in enumerate(row):
        if char == '#':
            galaxies.append((row_index, col_index))
print(galaxies)
print(len(galaxies))
galaxy_combinations = list(itertools.combinations(galaxies, 2))
print(len(list(galaxy_combinations)))
def manhattan_distance(pair):
    (x1, y1), (x2, y2) = pair
    return abs(x1-x2)  + abs(y1 - y2)
total = 0
for pair in (galaxy_combinations):
    total += manhattan_distance(pair)
print(total)
#print(galaxy_combinations)
