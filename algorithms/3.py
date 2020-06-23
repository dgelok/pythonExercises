# 3. Fibonacci Sequence
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

myList = [1, 2]
while True:
    new = myList[-1] + myList[-2]
    if new < 4000000:
        myList.append(new)
    else:
        break

sum = 0
for num in myList:
    if num % 2 == 0:
        sum += num

print(sum)


