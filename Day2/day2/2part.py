# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def game2(input):
    #opponent rock
    if input[0] == 'A':
        #rock
        #need to lose
        if input[2] == 'X':
            return 0+3
        #paper
        #need to tie
        elif input[2] == 'Y':
            return 3+1
        #scissors
        #need to win
        elif input[2] == 'Z':
            return 6+2
    # opponent paper
    if input[0] == 'B':
        #rock
        #need to lose
        if input[2] == 'X':
            return 0+1
        #paper
        #need to tie
        elif input[2] == 'Y':
            return 3+2
        #scissors
        #need to win
        elif input[2] == 'Z':
            return 6+3
    # opponent scissors
    if input[0] == 'C':
        #rock
        #need to lose
        if input[2] == 'X':
            return 0+2
        #paper
        #need to tie
        elif input[2] == 'Y':
            return 3+3
        #scissors
        #need to win
        elif input[2] == 'Z':
            return 6+1

with open(r"C:\\Users\\rizar\\Documents\\PY PROGRAMMING\\AdventCode2022\\day2\\input2.txt","r") as input:
    score = 0
    for lines in input:
        score+=int(game2(lines))
    print(score)