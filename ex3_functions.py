
#1
def madlib(name="Billiam", subject="Zymurgy"):
    return f"It is my nemesis, {name}! I will defeat you with {subject}!"

#2
def cToF(degreesC):
    return degreesC * 9/5 + 32

#3
def fToC(degreesF):
    return (degreesF - 32) * 5/9

#4
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

#5
def isOdd(num):
    if not isEven(num):
        return True
    else:
        return False

#6
def onlyEvens(alist):
    final = []
    for item in alist:
        if isEven(item):
            final.append(item)
    return final

#7
def onlyOdds(alist):
    final = []
    for item in alist:
        if isOdd(item):
            final.append(item)
    return final

####### Medium Exercises ########

#1
def findSmallest(alist):
    mymin = alist[0]
    for item in alist:
        if item < mymin:
            mymin = item
    return mymin

# print(findSmallest(s))

#2
def findLargest(alist):
    mymax = alist[0]
    for item in alist:
        if item > mymax:
            mymax = item
    return mymax

# s = [1,4,7,9,-5,-2,78,-56,34]
# print(findLargest(s))

#3
def findShortest(x):
    min = x[0]
    for s in x:
        if len(s) < len(min):
            min = s
    return min

# n = ["one", "a", "b", "asdf", "aslkdfaslfj", "df", "asdf"]
# print(findShortest(n))

#4
def findLongest(x):
    max = x[0]
    for s in x:
        if len(s) > len(max):
            max = s
    return max

# print(findLongest(n))