# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def sieve(n):
    nums = [True for i in range(n+1)]

    answer = 0    
    p = 2
    while (p*p <= n):
        if (nums[p] == True):
            for i in range(p*2, n+1, p):
                nums[i] = False
        p += 1

    for k in range(2, n):
        if nums[k]:
            answer += k    

    print(answer)


sieve(2000000)