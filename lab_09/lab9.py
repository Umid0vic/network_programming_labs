# Network programming lab 9 - Compression
# created by Osman Said, 06-12-2021

import sys
import math
import random
import zlib

def readSweText(textFile):
    with open(textFile, 'r') as file:
        text = file.read()

    byteArr = bytearray(text, "utf-8")
    return byteArr


def task1(byteArr):
    print("task1")
    print('size of byteArr:' , len(byteArr))
    x = byteArr.decode("utf-8")
    print('size of text string:', len(x))


def makeHisto(byteArr):
    histo = {}
    for i in range(0,256):
        histo[i] = 0

    for i in byteArr:
        histo[i] += 1
    return histo
    

#Probality distribution (PD)
def makeProb(histo):
    histoSum = 0
    for i in histo:
        histoSum += histo[i]

    for i in histo:
        if histo[i] > 0:
            histo[i] = histo[i] / histoSum
    return histo


#Entropi of PD
def entropi(prob):
    h = 0
    for i in prob:
        if prob[i] != 0:
            l = math.log2(1 / prob[i])
            h += prob[i] * l
    return h


def copy(theCopy):
    random.shuffle(theCopy)    
    return theCopy

#----------------------------------#
x = readSweText('exempeltext.txt')
task1(x)
print('HISTOGRAM:', makeHisto(x))
print('ENTROPI:', entropi(makeProb(makeHisto(x))))

code1 = zlib.compress(x)
code2 = zlib.compress(copy(x))

print('Not compressed in bits: {}, in bytes: {}'.format((len(x)*8), len(x)))
print('Compressed in bits: {}, in bytes: {}'.format((len(code1)*8), len(code1)))
print('Shuffled compressed in bits: {}, in bytes: {}'.format((len(code2)*8), len(code2)))

t1 = """I hope this lab never ends because it is so incredibly thrilling!"""
t10 = 10*t1
print('len of symbols in t1 is {} and t10 is {}'.format(len(t1),len(t10)))

bt1 = bytearray(t1,'LATIN-1')
bt10 = bytearray(t10,'LATIN-1')

zt1 = zlib.compress(bt1)
zt10 = zlib.compress(bt10)

print('t1  not compressed bytes:{}, compressed bytes:{}, {}: bits  '.format(len(bt1),len(zt1),len(zt1)*8))
print('t10 not compressed bytes:{}, bytes:{}, {} :bits  '.format(len(bt10),len(zt10),len(zt10)*8))

et1= (len(zt1)*8)/ len(bt1)
et10= (len(zt10)*8) / len(bt10)
print(' t1 {} bites/symbol \nt10 {} bites/symbol'.format(et1,et10))

