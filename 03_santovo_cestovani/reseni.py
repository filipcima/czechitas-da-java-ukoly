def main():
    instructions = [('R', 5), ('L', 5), ('R', 5), ('R', 3)]
    position = [0, 0]
    direction = 0
    for ins in instructions:
        if ins[0] == 'L':
            direction -= 1 % 4
        else:
            direction += 1 % 4

        if direction == 0:  # north
            position[1] += ins[1]
        if direction == 3:  # west
            position[0] -= ins[1]
        if direction == 2:  # south
            position[1] -= ins[1]
        if direction == 1:  # east
            position[0] += ins[1]

    return abs(position[0] + position[1])

