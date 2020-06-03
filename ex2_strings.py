# All initial inputs can be replaced with var = input(###)

#1

# myString = "Hello, World!"
# final = myString.upper()
# print(final)

#2 (assuming this meant lowercased)

# myString = "Hello, World!"
# final = myString.lower()
# print(final)

#3

# myString = "Hello, World!"
# final = ""
# for i in range(len(myString)):
#     final = myString[i] + final
# print(final)

#4
# A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7 

# myPar = "Lorem ipsum dolor BOOGERS etur! adipisicing elit. Nisi fugit quaerat quisquam labore. Maiores, enim libero nisi aliquid voluptatem dignissimos sit saepe, velit reprehenderit, quos exercitationem eius nihil alias dolores!"
# newPar = ""
# for i in range(len(myPar)):
#     if myPar[i] == "A" or myPar[i] == "a":
#         newPar += "4"
#     elif myPar[i] == "E" or myPar[i] == "e":
#         newPar += "3"
#     elif myPar[i] == "G" or myPar[i] == "g":
#         newPar += "6"
#     elif myPar[i] == "I" or myPar[i] == "i":
#         newPar += "1"
#     elif myPar[i] == "O" or myPar[i] == "o":
#         newPar += "0"
#     elif myPar[i] == "S" or myPar[i] == "s":
#         newPar += "5"
#     elif myPar[i] == "T" or myPar[i] == "t":
#         newPar += "7"
#     else:
#         newPar += myPar[i]
# print(newPar)

#5

# word = "Lilly"
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# final = ""
# for i in range(len(word)):
#     if word[i] in vowels:
#         if word[i] == word[i+1]:
#             final += word[i]*4
#         else:
#             final += word[i]
#     else:
#         final += word[i]
# print(final)

#6

alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = alphabet.upper()
myMessage = input("What would you like to encode? > ")
encoded = ""
for i in range(len(myMessage)):
    if myMessage[i] in alphabet:
        encoded += 
    elif myMessage[i] in ALPHABET:
        pass
    else:
        encoded += myMessage[i]
