file = "data.txt"
#file = "sample.txt"
data = [list(line.strip()) for line in open(file, 'r').readlines()]
print(data)
width, height = len(data[0]), len(data)
print (width, height)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f'({self.x}, {self.y})'
class Beam:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    def move(self):
        self.position = self.position + self.velocity
    def __str__(self):
        return f'position: {self.position}  velocity: {self.velocity}'
    def rotate_left(self):
        print(f'inside rotate_left before rotation velocity: {self.velocity}')
        self.velocity = Vector(self.velocity.y, -1 * self.velocity.x)
        print(f'inside rotate_left after rotation velocity: {self.velocity}')
    def rotate_right(self):
        self.velocity = Vector(-1 * self.velocity.y, self.velocity.x)
    def orient(self):
        x, y = self.position.x, self.position.y
        split = False
        value = data[y][x]
        match value:
            case '\\':
                print(' \\ encountered')
                if self.velocity.y == 0:
                    self.rotate_right()
                elif self.velocity.x == 0:
                    self.rotate_left()
            case '/':
                print('/ encountered')
                if self.velocity.y == 0:
                    print('rotating left')
                    self.rotate_left()
                elif self.velocity.x == 0:
                    self.rotate_right()
                print(f'velocity now: {self.velocity}')
            case '|':
                if self.velocity.x:
                    self.rotate_right()
                    split = True

            case '-':
                if self.velocity.y:
                    self.rotate_right()
                    split = True

        return split


    def out_of_bounds(self):
        x, y = self.position.x, self.position.y
        if x < 0 or y < 0 or x == width or y == height:
            return True
        return False

beams = []
visited = set()
energized = set()
position = Vector(-1,0)
velocity = Vector(1,0)
beams.append(Beam(position, velocity))
beamNumber = 0
while beams:
    beam = beams[0]
    beam.move()
    print(beam)
    if beam.out_of_bounds():
        beams.remove(beam)
        print("beam has exited the grid")
        continue
    if (beam.position.x, beam.position.y, beam.velocity.x, beam.velocity.y) in visited:
        beams.remove(beam)
        print("been here moving this way before")
        continue
    energized.add(beam.position)
    visited.add((beam.position.x, beam.position.y, beam.velocity.x, beam.velocity.y))
    split = beam.orient()
    if split:
        beams.append(Beam(beam.position, Vector(-beam.velocity.x , -beam.velocity.y)))
        beamNumber += 1
        print(f'creating new beam number: {beamNumber}')

print(f'answer: {len(energized)}')
for item in visited:
    print(item)


grid = [['.' for n in range(width)] for i in range(height)]
print(grid)
for (x, y, *z) in visited:
    grid[y][x] = '#'
for line in grid:
    print(''.join(line))
answer = 0
for line in grid:
    answer += line.count('#')
print(answer)











