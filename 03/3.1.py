import re
chars = open("input.txt", 'r').read()
symbols = {char for char in chars if char.isdigit() is False and char != '.' and char != '\n'}
data = chars.split('\n')
regex = re.compile("\\d+")
rows, columns = len(data), len(data[0])
def getNeighbors(row, span):
    neighbors = []
    for n in range(span[0] -1 , span[1] + 1 ):
        neighbors.append((n, row -1))
        neighbors.append((n, row + 1))
    neighbors.append((span[0]-1, row))
    neighbors.append((span[1], row))
    neighbors = [item for item in neighbors if isInBounds(item)]
    return neighbors

def checkNeighbors(neighbors):
    for x, y in neighbors:
        if data[y][x] in symbols:
            return True
    return False

def isInBounds(coord):
    x, y = coord
    return all([x >= 0, x < columns, y >= 0, y< rows])

numbers = []
for n in range(rows):
    matches = regex.finditer(data[n])
    for match in matches:
        numbers.append((n, match.span(), int(match[0])))
print(sum([item[2] for item in numbers if checkNeighbors(getNeighbors(item[0], item[1]))]))
