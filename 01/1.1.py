import re
file = open("01.txt", 'r')
data = [line for line in file]
digits = [re.findall(r'\d', line) for line in data]
digits = [[line[0], line[-1]] for line in digits]
digits = ([int(''.join(line)) for line in digits])
print(sum(digits))
