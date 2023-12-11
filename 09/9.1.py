file = "input.txt"
data = open(file, 'r').readlines()
data = [[int(x) for x in line] for line in [line.split() for line in data]]
def diff(numbers):
    diffed = []
    for n in range(len(numbers) -1):
        diffed.append(numbers[n+1] - numbers[n])
    return diffed
answer = 0
for number_list in data:
    lists = [number_list]
    while any(lists[-1]):
        current_list = lists[-1]
        lists.append(diff(current_list))

    while  any(lists[-1]):
        current_list = lists[-1]
    for list in lists:
        answer += list[-1]
print(answer)
