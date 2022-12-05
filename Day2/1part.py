file = open(r"C:\\Users\\rizar\\Documents\\PY PROGRAMMING\\AdventofCode2022\\day2\\input2.txt","r")

def part1():
    score = 0
    for row in file:
        op, me = row.replace("\n","").split(" ")
        if me == "X":
            score += 1
        elif me == "Y":
            score += 2
        else:
            score += 3        
        
        if ord(me) - ord(op) == 23:
            score += 3
        elif ord(me) - ord(op) == 24 or ord(me) - ord(op) == 21:
            score += 6

    print(score)

part1()
'''
Unicode is the table lists all of the characters used in human languages; it assigns each character a unique code number.
ord() method return Unicode code for a character;

'''