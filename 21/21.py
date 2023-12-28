file = "data.txt"
data = open(file, 'r').readlines()
data = [[char for char in line.strip()]  for line in data]
possible_gardens = set() #where you could be after each step
width, height = len(data[0]), len(data)
gardens = set()
rocks = []
for y in range(height):
    for x in range(width):
        match data[y][x]:
            case '.':
                gardens.add((x,y))
            case '#':
                rocks.append((x,y))
            case 'S':
                start = ((x,y))
                gardens.add(start)
                possible_gardens.add(start)

def take_a_step(possible_gardens):
    #returns all valid garden locations after one more step
    garden_neighbors = set()
    for location in possible_gardens:
        new_neighbors = find_garden_neighbors(*location)
        garden_neighbors |= new_neighbors
    return garden_neighbors

def find_garden_neighbors(x, y):
    #returns a set of all valid neighbors that are gardens
    candidates = [(x + a, y + b) for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    candidates = [pair for pair in candidates if pair[0] > -1 and pair[1] > -1]
    candidates = [pair for pair in candidates if pair[0] < width and pair[1] < height]
    garden_neighbors = [pair for pair in candidates if pair in gardens]
    return set(garden_neighbors)

for n in range(64):
    possible_gardens = take_a_step(possible_gardens)
    n += 1
print(len(possible_gardens))