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
    this_sum = 0
    lists = [number_list]
    while  any(lists[-1]):
        current_list = lists[-1]
        lists.append(diff(current_list))
    for n in range(len(lists)-1,0,-1):
        lists[n-1].insert(0, lists[n-1][0] - lists[n][0])
    answer += lists[0][0]
print(answer)
