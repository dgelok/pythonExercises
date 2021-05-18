import math
def decrypt(encrypted_text, n):
    answer = encrypted_text
    for i in range(0, n):
        part1 = answer[:math.floor(len(answer)/2)]
        part2 = answer[math.floor(len(answer/2)):]
        answer = ""
        for j in range(0, len(answer)):
            answer += part1[j] + part2[j]

    return answer



def encrypt(text, n):
    answer = text
    for i in range(0, n):
        part1 = answer[1::2]
        part2 = answer[0::2]
        answer = part1 + part2

    return answer