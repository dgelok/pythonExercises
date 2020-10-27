def filter_list(l):
#   'return a new list with the strings filtered out'
    answer = []
    for i in l:
        if isinstance(i, int):
            answer.append(i)
    return answer


thing = [1,2,3,'a','b',]
print(filter_list(thing))