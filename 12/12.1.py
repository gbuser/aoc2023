import re
import itertools
data = open("input.txt", 'r').readlines()
data = [line.split() for line in data]
data = [{'springs':sequence, 'groups': [int(x) for x in group.split(',')]} for sequence, group in data ]
def find_QMs( line):
    springs = line['springs']
    QMs = [ index for index, value in enumerate(springs) if value =="?"]
    return QMs

def QMs_to_hash(line):
    result = sum(line['groups'])- line['springs'].count('#')
    return result

def convert_springs(springs, combo):
    converted = ''
    for index, value in enumerate(springs):
        if value == '?':
            converted += ('#' if index in combo else '.')
        else:
            converted += value
    return converted

def make_regex(groups):
    regex = ''
    for group in groups:
        regex += "#{" + str(group) + "}.+"
    return regex[:-2]

tally = 0
for line in data:
    QMs = find_QMs(line)
    QMs_to_hashes = QMs_to_hash(line)
    combos = list(itertools.combinations(QMs,QMs_to_hashes))
    regex = make_regex(line['groups'])
    for combo in combos:
        converted = convert_springs(line['springs'], combo)
        if re.search(regex, converted):
            tally += 1
print(tally)


