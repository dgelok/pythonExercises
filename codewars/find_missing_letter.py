def find_missing_letter(chars):
    alph = "abcdefghijklmnopqrstuvwxyz"

    for i in range(0, len(chars)-1):
        myLetter = chars[i]
        nextLetter = chars[i+1]
        myIndex = alph.index(myLetter.lower())
        if nextLetter.lower() != alph[myIndex + 1]:
            answer = alph[myIndex + 1]
            if myLetter.islower():
                return answer
            else:
                return answer.capitalize()
            

