# #1
# name = input("Hello! What is your name? ")
# print(f"Hello, {name}! Nice to meet you.")

# #2
# name = input("WHAT IS YOUR NAME, PUNK???? ")
# name = name.upper()
# print(f"OH YEAH? YOUR NAME IS {name}???")
# print(f"WELL GUESS WHAT - YOUR NAME HAS {len(name)} CHARACTERS!")

# #3
# noun1 = input("Noun: ")
# noun2 = input("Another Noun: ")
# adverb1 = input("Adverb: ")
# adverb2 = input("Another adverb: ")
# adjective1 = input("Adjective: ")
# exclaimation = input("Exclaimation: ")
# madlib = "While walking through a {} {}, you see a {}. '{}!', you {} shout. 'That\'s a {}!' Then you die, {}.".format(adjective1, 
# noun1, noun2, exclaimation, adverb1, noun2, adverb2)
# print(madlib)

# # 73.0
# # 82
# # 2

# #4
# day = int(input('Day (0-6)? '))
# dayref = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# print(dayref[day])


# #5
# day = int(input('Day (0-6)? '))
# dayref = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# if day == 0 or day == 6:
#     print("Sleep in!")
# else:
#     print("Go to work!")

# #6
# cTemp = input("temperature in celsius? > ")
# fTemp = int(cTemp) * 1.8 + 32
# print(f"{fTemp} F")

#7

mealPrice = int(input("How much was the meal? > "))
serviceLevel = input("How was the service? > ")
if serviceLevel == 'good':
    tipamount = .20
elif serviceLevel == "fair":
    tipamount = .15
else:
    tipamount = .10
total = mealPrice * tipamount + mealPrice
print(f"Your tip amount is ${tipamount}.")
print(f"Your total is ${total}.")
