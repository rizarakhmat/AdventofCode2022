def RuckSackReorder(compartments):
    total = 0
    memory = set()
    for compartment in compartments:
        length = len(compartment)
        mid = length // 2
        for item in range(0,mid):
            memory.add(compartment[item])

        for item in range(mid,length):

            if compartment[item] in memory:
                if compartment[item].isupper():
                    value = (ord(compartment[item]) - 64) + 26 #use Unicode to prioritize items Uppercase
                else:
                    value = ord(compartment[item]) - 96 #use Unicode to prioritize items Lowercase
                memory.clear()

        total += value
    return total



if __name__ == '__main__':
    file = open(r"C:\\Users\\rizar\\Documents\\PY PROGRAMMING\\AdventofCode2022\\day3\\input3.txt","r")
    elves = file.readlines()
    print(RuckSackReorder(elves))