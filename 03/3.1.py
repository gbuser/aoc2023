import re
chars = open("input.txt", 'r').read()
symbols = {char for char in chars if not any([char.isdigit(), char == '.', char == '\n'])}
data = chars.split('\n')
regex = re.compile("\\d+")
rows, columns = len(data), len(data[0])

def getNeighbors(row, span): #find all neigbors in bounds
    neighbors = []
    for n in range(span[0] -1 , span[1] + 1 ):
        neighbors.append((n, row -1))
        neighbors.append((n, row + 1))
    neighbors.append((span[0]-1, row))
    neighbors.append((span[1], row))
    neighbors = [item for item in neighbors if isInBounds(item)] #remove invalid
    return neighbors

def neighbors_has_symbol(neighbors):
    for x, y in neighbors:
        if data[y][x] in symbols:
            return True
    return False

def isInBounds(coord):
    x, y = coord
    return all([x >= 0, x < columns, y >= 0, y< rows])

numbers = []
for row in range(rows): #get row, span, value of every number
    matches = regex.finditer(data[row])
    for match in matches:
        numbers.append((row, match.span(), int(match[0])))
print(sum([value for row, span, value in numbers if neighbors_has_symbol(getNeighbors(row, span))]))
