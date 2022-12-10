def part1():
    file = open(r"C:\\Users\\rizar\\Documents\\PY PROGRAMMING\\AdventofCode2022\\Day5\\input5.txt","r")
    next = False
    stacks = [[],[],[],[],[],[],[],[],[]]
    for row in file:
        if row == "\n":
            next = True
        elif next == False:
            for i in range(0,len(row),4): #range(start, stop, step)??? 0 4 8 12 16
                for j in range(0,4): # 0 1 2 3
                    if row[i+j] != " " and row[i+j] != "[" and row[i+j] != "]" and row[i+j] != "\n" and row[i+j] != "1" and row[i+j] != "2" and row[i+j] != "3":
                        stacks[int(i/4)].append(row[i+j])
        else:
            rowList= row.replace("\n","").split(" ")
            for _ in range(0,int(rowList[1])):
                tmp = stacks[int(rowList[3])-1].pop(0)
                stacks[int(rowList[5])-1].insert(0,tmp)
        # print(stacks)
    for s in stacks:
        print(s[0])
part1()