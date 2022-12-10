import re

def StartOfPacketMarker(lines):
    for line in lines:
        for char in range(0, len(line)):
            num = line[char: char + 4] #EX: rbcb, bcbl, cbls;
            numSet = set(num) #EX: {'c', 'b', 'l'} 
            # set() method is used to convert any of the iterable to sequence to with distinct (отдельный) elements
            # An iterable is any Python object capable of returning its members one at a time
            if len(numSet) == len(num):
                return char + 4


if __name__ == '__main__':
    file = open('input6.txt', 'r')
    elves = file.readlines()
    print(StartOfPacketMarker(elves))