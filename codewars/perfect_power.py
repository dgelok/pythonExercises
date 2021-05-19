# def isPP(n):
#     import math
#     for i in range(1, math.floor(math.sqrt(n))):
#         for j in range(1, math.floor(math.sqrt(n))):
#             if i**j == n:
#                 return [i,n]
#             elif i**j > n:
#                 break

#     return None


from math import ceil, log, sqrt

def isPP(n):
    for b in range(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None