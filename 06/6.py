import re
data = [[int(x) for x in re.findall('\\d+', line)] for line in open("input.txt", 'r').readlines()]
data = list(zip(data[0], data[1]))
prod = 1
for time, record in data:
    count = 0
    for charge_time in range(time):
        if charge_time * (time - charge_time) > record:
            count += 1
    prod *= count
print(prod)

time =int(''.join([str(x[0]) for x in data]))
record = int(''.join([str(x[1]) for x in data]))
count = 0
for charge_time in range(time):
    if charge_time * (time - charge_time) > record:
        count += 1
print(count)