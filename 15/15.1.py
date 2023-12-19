file = "data.txt"
#file = "sample.txt"
data = open(file, 'r').read().split(',')
data = [[ord(letter) for letter in line] for line in data]
def hash(ords):
    current_value = 0
    for number in ords:
        current_value = ((current_value + number) * 17)%256
    return current_value
hashsum = 0
for item in data:
    hashsum += hash(item)
print(hashsum)