import math

def zero(p1 = None): 
    if p1 == None:
        return 0
    return calcme(p1, 0)
def one(p1 = None): 
    if p1 == None:
        return 1
    return calcme(p1, 1)
def two(p1 = None): 
    if p1 == None:
        return 2
    return calcme(p1, 2)    
def three(p1 = None): 
    if p1 == None:
        return 3
    return calcme(p1, 3)
def four(p1 = None): 
    if p1 == None:
        return 4
    return calcme(p1, 4)

def five(p1 = None): 
    if p1 == None:
        return 5
    return calcme(p1, 5)

def six(p1 = None): 
    if p1 == None:
        return 6
    return calcme(p1, 6)

def seven(p1 = None): 
    if p1 == None:
        return 7
    return calcme(p1, 7)

def eight(p1 = None): 
    if p1 == None:
        return 8
    return calcme(p1, 8)

def nine(p1 = None): 
    if p1 == None:
        return 9
    return calcme(p1, 9)

def plus(num):
    return ["add", num]
def minus(num):
    return ["minus", num] 
def times(num):
    return ["times", num] 
def divided_by(num):
    return ["divide", num] 

def calcme(p1, p2):
    if p1[0] == "add":
        return math.floor(p2 + p1[1])
    elif p1[0] == "minus":
        return math.floor(p2 - p1[1])
    elif p1[0] == "times":
        return math.floor(p2 * p1[1])    
    elif p1[0] == "divide":
        return math.floor(p2 / p1[1])
