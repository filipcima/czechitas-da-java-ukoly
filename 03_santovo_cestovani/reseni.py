def main():
    instructions = []
    file_str = ''
    with open('instrukce.txt', 'r') as fle:
        file_str = fle.read().replace('\n', '')
        file_str = file_str.replace(' ', '')
        instructions = file_str.split(',')
    print(instructions)
    position = [0, 0]
    file_str = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3"
    instructions = file_str.split(', ')
    direction = 0
    for ins in instructions:
        if ins[0] == 'L':
            direction = (direction - 1) % 4
        elif ins[0] == 'R':
            direction = (direction + 1) % 4
        print('direction is:', direction)
        if direction == 0:  # north
            position[1] += int(ins[1:])
        if direction == 3:  # west
            position[0] -= int(ins[1:])
        if direction == 2:  # south
            position[1] -= int(ins[1:])
        if direction == 1:  # east
            position[0] += int(ins[1:])
        print(ins[0], ins[1:])
        print(position)
        
    print(abs(0 - position[0]) + abs(0 - position[1]))
    return abs(0 - position[0]) + abs(0 - position[1])

if __name__ == '__main__':
    main()
