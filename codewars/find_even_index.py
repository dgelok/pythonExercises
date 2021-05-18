a = [20,10,-80,10,10,15,35]

def find_even_index(arr):
    for i in range(1, len(arr)):
        firstArr = arr[:i]
        lastArr = arr[i+1:]
        firstAccum = 0
        lastAccum = 0

        for j in range(0, len(firstArr)):
            firstAccum += firstArr[j]
        for j in range(0, len(lastArr)):
            lastAccum += lastArr[j]

        if firstAccum == lastAccum:
            return i

    return -1



print(find_even_index(a))