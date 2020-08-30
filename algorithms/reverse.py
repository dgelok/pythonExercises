s = "This is a coding question for reversing a string"
n = s.split(' ')
result = []

for i in n:
    if len(i) > 2:
        first = i[0]
        last = i[-1]
        lastnum = (len(i) - 1)
        # print(lastnum)
        mid = i[1:lastnum]
        new = ""
        for j in range(len(mid)):
            new = mid[j] + new
        result.append(first + new + last)
    else:
        result.append(i)

x = " ".join(result)
print(x)