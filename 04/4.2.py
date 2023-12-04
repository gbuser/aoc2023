from functools import reduce
data = [line.replace(':', '|').strip().split('|')[1:] for line in open("input.txt", 'r')]
data = [[a.strip().split(' '), b.strip().split(' ')] for a,b in data]
data = [[list(filter(None,a)), list(filter(None, b))] for a,b in data ]
data = [[{int(x) for x in a}, {int(y) for y in b}] for a, b in data]
data = [[x, 1] for x in [len(a.intersection(b)) for a,b in data]]
for n in range(len(data)):
    score, number = data[n]
    if score:
        for i in range(1, score +1):
            if n + i < len(data):
                data[n + i][1] += number
print(reduce(lambda a, b: a + b[1], data, 0))

