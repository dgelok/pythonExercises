def isPP(n):
    import math
    for i in range(1, math.floor(math.sqrt(n))):
        for j in range(1, math.floor(math.sqrt(n))):
            if i**j == n:
                return [i,n]
            elif i**j > n:
                break

    return None
