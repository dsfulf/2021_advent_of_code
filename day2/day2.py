with open('input.txt', 'r') as f:
    data = [i.strip().split(' ') for i in f.readlines()]


# part 1
unit: int

depth = 0
hz = 0

for direction, unit in data:
    unit = int(unit)
    if direction == 'forward':
        hz += unit
    elif direction == 'up':
        depth -= unit
    elif direction == 'down':
        depth += unit

print(depth)
print(hz)
print(depth * hz)


# part 2

aim = 0
depth = 0
hz = 0

for direction, unit in data:
    unit = int(unit)
    if direction == 'forward':
        hz += unit
        depth += unit * aim
    elif direction == 'up':
        aim -= unit
    elif direction == 'down':
        aim += unit

print(depth)
print(hz)
print(depth * hz)
