from stationeers_pytrapic.symbols import *

def range1(stop):
    a = 0
    for i in range(stop):
        a += i
    return a

def range2(start, stop):
    a = 0
    for i in range(start, stop):
        a += i
    return a

def range3(start, stop, step):
    a = 0
    for i in range(start, stop, step):
        a += i
    return a

def range1_const():
    a = 0
    for i in range(10):
        a += i
    return a

def range2_const():
    a = 0
    for i in range(5, 15):
        a += i
    return a

def range3_const():
    a = 0
    for i in range(2, 20, 3):
        a += i
    return a

while True:
    a = stack[0]
    b = stack[1]
    c = stack[2]
    db.Setting = range1(a)
    db.Setting = range2(a,b)
    db.Setting = range3(a,b,c)
    db.Setting = range1_const()
    db.Setting = range2_const()
    db.Setting = range3_const()
