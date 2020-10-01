def findme(x):
    if len(x) == 1:
        return 1
    elif len(x) == 2:
        if int(x) >26:
            return 1
        else:
            return 2
    

    else:
        nums = []
        answer = 0
        for i in range(len(x)):
            nums.append(x[i:i+2])
        for num in nums:
            if int(num) > 26:
                answer += 0
            else: answer += 1
        return answer


print(findme('123'))