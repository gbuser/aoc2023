file = "data.txt"
data = open(file, 'r').readlines()
data = [[char for char in line.strip()]  for line in data]
possible = set()
width, height = len(data[0]), len(data)
gardens = []
rocks = []
for y in range(height):
    for x in range(width):
        match data[y][x]:
            case '.':
                gardens.append((x,y))
            case '#':
                rocks.append((x,y))
            case 'S':
                start = ((x,y))
                gardens.append(start)
                possible.add(start)

def take_a_step(possible):
    garden_neighbors = set()
    for location in possible:
        new_neighbors = find_garden_neighbors(*location)
        garden_neighbors = garden_neighbors.union(new_neighbors)
    return garden_neighbors

def find_garden_neighbors(x, y):
    candidates = [(x + a, y + b) for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    candidates = [pair for pair in candidates if pair[0] > -1 and pair[1] > -1]
    candidates = [pair for pair in candidates if pair[0] < width and pair[1] < height]
    garden_neighbors = [pair for pair in candidates if pair in gardens]
    return set(garden_neighbors)

for n in range(64):
    possible = take_a_step(possible)
    n += 1
print(len(possible))
