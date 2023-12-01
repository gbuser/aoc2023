import regex as re
file = open("01.txt", 'r')
data = [line for line in file]
original = data.copy()
pattern = "one|two|three|four|five|six|seven|eight|nine|\\d"
digits = [re.findall(pattern, line, overlapped = True) for line in data]
digits = [[line[0], line[-1]] for line in digits]

numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
for line in digits:
    if line[0] in numbers:
        line[0] = numbers[line[0]]
    if line[1] in numbers:
        line[1] = numbers[line[1]]




digits = ([int(''.join(line)) for line in digits])
print(sum(digits))
