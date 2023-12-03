import re
data = [line.strip() for line in open("input.txt", 'r')]
rows, columns = len(data), len(data[0])
regex = re.compile("\\d+")
def getNeighbors(row, span):
    neighbors = []
    for n in range(span[0] -1 , span[1] + 1 ):
        neighbors.append((n, row -1))
        neighbors.append((n, row + 1))
    neighbors.append((span[0]-1, row))
    neighbors.append((span[1], row))
    neighbors = [item for item in neighbors if item[0]>=0 and item[0]<columns and item[1] >= 0 and item[1]< rows]
    return neighbors
def countGears(integer):
    row, span, value = integer
    neighbors = getNeighbors(row, span)
    for neighbor in neighbors:
        if neighbor in asterisks:
            asterisks[neighbor].append(value)

numbers = []
asterisks = {}
for row in range(rows):
    matches = regex.finditer(data[row])
    for match in matches:
        numbers.append((row, match.span(), int(match[0])))
    for index, char in enumerate(data[row]):
        if char == '*':
            asterisks[(index, row)] = []

for number in numbers:
    countGears(number)
answer = 0
for key, value in asterisks.items():
    if len(asterisks[key]) == 2:
        answer += value[0] * value[1]
print(answer)