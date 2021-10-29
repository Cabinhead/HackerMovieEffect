import random, time, os
from termcolor import colored

popamount = 5
coolnumber = 0
running = True
numberlist = []
clear = lambda: os.system('cls')

class Snapshot:
    def __init__(self, list):
        self.list = list

    def pop(self):
        randnum = random.randint(0,len(numberlist) - 1)
        if numberlist[randnum] !=" ":
            numberlist[randnum] =" "
        else:
            self.pop()

    def create(self):
        for i in range(popamount):
            self.pop()

def buildstructure():
    for i in range(16):
        Snapshot1 = Snapshot(numberlist)
        Snapshot1.create()
        print(colored(''.join(map(str, numberlist)), 'green'))

while True:
    numberlist = []
    for i in range(100):
        coolnumber = random.randint(0,1)
        numberlist.append(coolnumber)

    print(colored(''.join(map(str, numberlist)), 'green'))
    buildstructure()
    time.sleep(0.05)
    clear()