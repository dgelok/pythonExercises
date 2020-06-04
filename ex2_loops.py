# # I am assuming all user-generated input is within the scope of the question. 

# #1
# for i in range(1, 11):
#     print(i)

# #2
# start = int(input("Which number shall we start on? > "))
# end = int(input("Which number shall we end on? > "))

# for i in range(start, end+1):
#     print(i)

# #3
# for i in range(1, 10, 2):
#     print(i)

# ### OR ###

# for i in range(1, 10):
#     if i % 2 != 0:
#         print(i)

# #4
# for i in range(5):
#     print("*" * 5)

# #5
# num = int(input("How big is the square? > "))
# for i in range(num):
#     print("*" * num)

# #6
# height = int(input("How tall should the box be? > "))
# width = int(input("How wide should the box be? > "))
# for i in range(height):
#     if i == 0 or i == (height - 1):
#         print("*" * width)
#     else: 
#         print("*" + (" " * (width - 2) + "*"))


# #7 

height = 4
row = []
while (2*i) < height:
    newrow = " "*i
    i += 1

# # 8
# while True:
#     height = int(input("How high shall the tree be? > "))
#     if height < 0:
#         print("Sorry, we need a positive number.")
#     if height % 2 == 0:
#         print("Sorry, we need an odd number")
#     else:
#         break

# rows = []
# i = 0
# while 2*i < height:
#     newrow = " "*i + "*"*(height - i*2) + " "*i
#     rows.append(newrow)
#     i += 1

# index = len(rows)
# for x in range(len(rows)-1, 0, -1):
#     print(rows[x])

# #9
# for i in range(1,11):
#     for j in range(1, 11):
#         product = i * j
#         print(f"{i} X {j} = {product} ")

# #bonus1
# myMessage = input("What's your message? > ")
# length = len(myMessage)
# border = "*" * (length + 4)
# print(border)
# print(f"* {myMessage} *")
# print(border)

# #bonus 2
# triNums = []
# i = 1
# while len(triNums) < 100:
#     newNum = int(i*(i+1)/2)
#     triNums.append(newNum)
#     i+= 1
# print(triNums)


# #bonus 3
# myNum = int(input("Pick a number > "))
# factors = []
# for i in range(1, myNum):
#     if myNum % i == 0:
#         factors.append(i)
# print(factors)
