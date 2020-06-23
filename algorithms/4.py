


# 4. Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


mylist = []
n = 600851475143


for i in range(2,n):
    if n%i == 0:
        n = n / i
        mylist.append(i)

print(mylist)

factors 
def factor(num):
    for i in range(2,num):
        if num%i == 0:
            return (num / i)


