# # syntax error:
# a = 5print()

# print(a))


# # type error - 
# a = 5 + "ten"
# print(a)


# #import error
# import assdlfkjsdflkjsdlfkj

# #name error
# a = 5
# b = c


# #import error
# x = open('dlksdfjlksdjfsj.txt')


# #value error
# a = [1,2,3]
# a.remove(4)


# #index error
# a = [1,2,3]
# a[5]

# mydict = {'name': 'Max'}
# mydict["garbage"]

#raise exception
# x = -5
# if x < 0:
#     raise Exception("x should be positive")

# x = -5
# assert (x>=0)
# #or
# x = -5
# assert (x>0), "here's my message"

# #HANDLE EXCEPTIONS

# try:
#     a = 5 / 1
#     b = a + "hosdf"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else: 
#     print("all is fine")
# finally:
#     print("this always runs")


class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def testvalue(x):
    if x > 100:
        raise ValueTooHighError("value too high")
    if x < 5:
        raise ValueTooLowError("value is too SMALL", x)

try:
    testvalue(0)
except Exception as e:
    print(e) #doesn't print anything
except ValueTooLowError as e:
    print(e.message, e.value)