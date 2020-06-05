# I'm assuming all user input to correspond to the code in question.
# All outputs are printed for verification.


#1
def numberSums():
    nums = [4,5,1,4,8,3,6,0]
    sum = 0
    for num in nums:
        sum += num
    print(sum)

#2
def largestNumber():
    nums = [4,5,100,4,2,3,6,0]
    big = nums[0]
    for num in nums:
        if big < num:
            big = num
    print(big)

#3
def smallestNumber():
    nums = [4,5,100,4,-4,3,6,0]
    small = nums[0]
    for num in nums:
        if small > num:
            small = num
    print(small)

#4
def evenNums():
    nums = [4,5,100,4,-4,3,6,0]
    for num in nums: 
        if num % 2 == 0:
            print(num)

#5
def positiveNums():
    nums = [-4,-5,100,4,-4,3,6,0]
    for num in nums: 
        if num > 0:
            print(num)

#6
def positiveNums2():
    nums = [-4,-5,100,4,-4,3,6,0]
    positives = []
    for num in nums: 
        if num > 0:
            positives.append(num)
    print(positives)

#7

def multiList():
    myFactor = 12
    nums = [-4,-5,100,4,-4,3,6,0]
    final = []
    for num in nums:
        final.append(num * myFactor)
    print(final)


#8
def multiVector():
    list1 = [1,2,4]
    list2 = [3,3,6]
    final = []
    for i in range(len(list1)):
        final.append(list1[i]*list2[i])
    print(final)

#9

def matrixAdd():
    list1 = [[1, 3], [2, 4]]
    list2 = [[5, 2], [1, 0]]
    final = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            newnum = list1[i][j] + list2[i][j]
            final[i][j] = newnum
    print(final)


#10 --- ???

def matrixAdd2():
    list1 = [[1, 3], [2, 4]]
    list2 = [[5, 2], [1, 0]]
    final = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            newnum = list1[i][j] + list2[i][j]
            final[i][j] = newnum
    print(final)

#11
def deDup():
    nums = [-4,-5,100,4,100,6,-4,3,6,0]
    final = []
    for num in nums:
        if num not in final:
            final.append(num)
    print(final)

#bonus

question = 2
while True:
    if question == 1:
        numberSums()
        break
    elif question == 2:
        largestNumber() 
        break 
    elif question == 3:
        smallestNumber() 
        break
    elif question == 4:
        evenNums()
        break
    elif question == 5:
        positiveNums() 
        break
    elif question == 6:
        positiveNums2()  
        break 
    elif question == 7:
        multiList()
        break
    elif question == 8:
        multiVector() 
        break
    elif question == 9:
        matrixAdd() 
        break   
    elif question == 10:
        matrixAdd2() 
        break
    elif question == 11:
        deDup()
        break

    