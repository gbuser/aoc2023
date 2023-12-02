import re
data = [line.strip() for line in open("data.txt", 'r')]
maxRed, maxGreen, maxBlue = 12, 13, 14
pattern = "(\\d+) (red|blue|green)"
games = []
n = 1
for line in data:
    match = re.findall(pattern, line)
    cubes = {'game': n}
    for number, color in match:
        number = int(number)
        cubes.setdefault(color, number)
        if number > cubes[color]:
            cubes[color] = number
    games.append(cubes)
    n +=1
answer = 0
for item in games:
    answer += item['red'] * item['blue'] * item['green']
print(answer)