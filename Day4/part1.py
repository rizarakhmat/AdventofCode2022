def PairContainers(pairs):
    count = 0
    for pair in pairs:
        pair = pair.replace('\n', '') 
        # 7-24,8-8
        # 2-75,37-51
        # -> 7-24,8-82-75,37-51
        pair = pair.split(',')
        # -> [7-24],[8-82]
        pair1 = pair[0].split('-')
        # -> [7],[24]
        # Why not: pair = pair.split('-')? i think becouse you need to enter each list by specifying index
        pair2 = pair[1].split('-')
        # -> [8],[82]
        lower1 = int(pair1[0])
        upper1 = int(pair1[1])
        lower2 = int(pair2[0])
        upper2 = int(pair2[1])

        if (lower2 <= lower1 and upper1 <= upper2) or (lower1 <= lower2 and upper2 <= upper1):
        # 2-8 fully contains 3-7
        # 6-9 if fully contaied by 4-12 
            count += 1

    return count
        
if __name__ == '__main__':
    file = open(r"C:\\Users\\rizar\\Documents\\PY PROGRAMMING\\AdventofCode2022\\Day4\\input4.txt","r")
    elves = file.readlines()
    print(PairContainers(elves))
        


