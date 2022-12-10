import re
'''
[T]             [P]     [J]        
[F]     [S]     [T]     [R]     [B]
[V]     [M] [H] [S]     [F]     [R]
[Z]     [P] [Q] [B]     [S] [W] [P]
[C]     [Q] [R] [D] [Z] [N] [H] [Q]
[W] [B] [T] [F] [L] [T] [M] [F] [T]
[S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
[Q] [Q] [B] [D] [J] [W] [H] [R] [J]
 1   2   3   4   5   6   7   8   9 
'''
memory = [['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
          ['V', 'W', 'J'],
          ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
          ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
          ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
          ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
          ['D', 'H', 'G', 'M', 'R'],
          ['H', 'N', 'M', 'V', 'Z', 'D'],
          ['G', 'N', 'F', 'H']
          ]

def CrateRearangment(instructions):
    topCrates = []
    for line in instructions:
        line = re.sub(r'[^0-9]', '', line) # move 3 from 4 to 9 -> 349
        if len(line) == 3:
            move = int(line[0])
            From = int(line[1]) - 1
            To = int(line[2]) - 1
        else:
            move = int(line[0] + line[1]) # ERROR: string index out of range
            From = int(line[2]) - 1
            To = int(line[3]) - 1
        
        for _ in range(0, move):
            memory[To].append(memory[From].pop()) # ['V', 'Z', 'D'], ['F', 'H']] ->['V', 'Z'], ['F', 'H', 'D']]
    for item in memory:
        topCrates.append(item.pop())
    return(topCrates)

if __name__ == '__main__':
    file = open(r"C:\\Users\\rizar\\Documents\\PY PROGRAMMING\\AdventofCode2022\\Day5\\input5.txt","r")
    elves = file.readlines()
    print(CrateRearangment(elves))