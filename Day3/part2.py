def convertToPriority(item):
    if item.isupper():
        value = (ord(item) - 64) + 26
    else:
        value = ord(item) - 96
    return value

def part2():
    file = [row for row in open(r"C:\\Users\\rizar\\Documents\\PY PROGRAMMING\\AdventofCode2022\\day3\\input3.txt","r")]
    types = 0
    for i in range(0,len(file),3):
        for c in file[i]:
            if c in file[i+1] and c in file[i+2]:
                types += convertToPriority(c)
                break
    print(types)

part2()