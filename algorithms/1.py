

# 1. Fizz Buzz
# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".


for num in range(101):
    if num % 5 == 0 and num % 3 == 0:
        print(str(num)+"FizzBuzz")
    elif num % 3 == 0:
        print(str(num)+"Fizz")
    elif num % 5 == 0:
        print(str(num)+"Buzz")
    else:
        print(num)



