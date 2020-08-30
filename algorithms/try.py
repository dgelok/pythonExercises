def filledOrders(order, k):
    sortedOrders = sorted(order)
    answer = 0

    while k >= 0:
        for i in range(len(sortedOrders)):
            if sortedOrders[i] <= k:
                answer += 1
                k -= sortedOrders[i]
        break
    
    return answer 

a = 3
order = [5,4,6]
answer = filledOrders(order, a)
print(answer)