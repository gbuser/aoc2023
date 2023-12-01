import re
data = [line for line in open("01.txt", 'r')]
digits = [re.findall(r'\d', line) for line in data]
digits = [[line[0], line[-1]] for line in digits]
digits = ([int(''.join(line)) for line in digits])
print(sum(digits))
