#/usr/local/bin/python
from __future__ import print_function
import random

chorusText = random.choice(open('input.txt').readlines())
numChorusRepeats = random.randint(2,4)



for x in range(4,10): #4-10 verses
    for y in range(0,random.randint(3,8)): #3-8 lines per verse
        print(random.choice(open('input.txt').readlines()), end='') #print verse
    for z in range(0, numChorusRepeats):
        print(chorusText, end='') #print chorus
    print("\n\n")
