from collections import defaultdict
import sys
import math
from string import ascii_uppercase as letters

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    with open (filename,encoding='utf-8') as f:
        text = f.read().upper()
        X = dict((l, text.count(l)) for l in letters)
    return X

def qOne(letterCount):
    print('Q1')
    for k, v in letterCount.items():
        print(k, v)

def qTwo(letterArray, e, s):
    print('Q2')
    print(f"{letterArray[0]*(math.log(e[0])):.4f}")
    print(f"{letterArray[0]*(math.log(s[0])):.4f}")

def qThree(letterArray, e, s):
    fE = math.log(0.6)
    for i in range(26):
        fE += letterArray[i]*(math.log(e[i]))
    fS = math.log(0.4)
    for i in range(26):
        fS += letterArray[i]*(math.log(s[i]))
    print('Q3')
    print(f"{fE:.4f}",)
    print(f"{fS:.4f}")
    qFour(fE, fS)

def qFour(fE, fS):

    if fS - fE >= 100:
        pE = 0
    elif fS - fE <= -100:
        pE = 1
    else:
        pE = 1/(1+math.exp(fS-fE))
    print('Q4')
    print(f"{pE:.4f}")

def main():
    print(sys.argv)
    letterCount = shred('letter.txt')
    qOne(letterCount)
    e,s = get_parameter_vectors()
    letterArray = list(letterCount.values())
    qTwo(letterArray, e, s)
    qThree(letterArray, e, s)

main()
