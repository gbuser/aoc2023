import functools
data = [line.replace(':', '|').strip().split('|')[1:] for line in open("input.txt", 'r')]
data = [[a.strip().split(' '), b.strip().split(' ')] for a,b in data]
data = [[list(filter(None,a)), list(filter(None, b))] for a,b in data]
data = [[{int(x) for x in a}, {int(y) for y in b}] for a, b in data]
data = list(filter(None, [len(a.intersection(b)) for a,b in data]))
print(functools.reduce(lambda a, b: a + 2**(b-1), data, 0))