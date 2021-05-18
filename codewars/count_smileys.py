def count_smileys(arr):
    answers = 0
    for i in range(0, len(arr)):
        if arr[i][0] == ":" or arr[i][0] == ";":
            if arr[i][-1] == "D" or arr[i][-1] == ")":
                if arr[i][1] == "-" or arr[i][1] == "~" or len(arr[i]) == 2:
                    answers += 1
    
    return answers