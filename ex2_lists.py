# I'm assuming all user input to correspond to the code in question.
# All outputs are printed for verification.


#1
nums = [4,5,1,4,8,3,6,0]

sum = 0
for num in nums:
    sum += num
print(sum)

#2
nums = [4,5,100,4,2,3,6,0]
big = 0
for num in nums:
    if big < num:
        big = num
print(big)

#3
nums = [4,5,100,4,-4,3,6,0]
small = 0
for num in nums:
    if small > num:
        small = num
print(small)

#4
nums = [4,5,100,4,-4,3,6,0]
for num in nums: 
    if num % 2 == 0:
        print(num)

#5
nums = [-4,-5,100,4,-4,3,6,0]
for num in nums: 
    if num > 0:
        print(num)

#6
nums = [-4,-5,100,4,-4,3,6,0]
positives = []
for num in nums: 
    if num > 0:
        positives.append(num)
print(positives)

#7

myFactor = 12
nums = [-4,-5,100,4,-4,3,6,0]
final = []
for num in nums:
    final.append(num * myFactor)
print(final)


#8
list1 = [1,2,4]
list2 = [3,3,6]
final = []
for i in range(len(list1)):
    final.append(list1[i]*list2[i])
print(final)

#9

list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]
final = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        newnum = list1[i][j] + list2[i][j]
        final[i][j] = newnum
print(final)


#10 --- ???

list1 = [[1, 3], [2, 4]]
list2 = [[5, 2], [1, 0]]
final = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        newnum = list1[i][j] + list2[i][j]
        final[i][j] = newnum
print(final)

#11

nums = [-4,-5,100,4,100,6,-4,3,6,0]
final = []
for num in nums:
    if num not in final:
        final.append(num)
print(final)

bonus