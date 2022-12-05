file = open(r"C:\Users\rizar\Documents\PY PROGRAMMING\AdventofCode2022\day1\input1.txt", "r")
output = [0]

def part1():
    i = 0
    for row in file:
        if row == "\n":
            i += 1
            output.append(0)
        else:
            output[i] += int(row)
    print(max(output))

part1()


def part2():
    top = sorted(output, reverse = True)
    top_3 = top[:3]
    print(sum(top_3))

part2()
