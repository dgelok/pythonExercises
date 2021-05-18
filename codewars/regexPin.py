
a = "woiejf"
b = "123"


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        testcase = "0123456789"
        for i in range(0, len(pin)): 
            if testcase.find(pin[i]) == -1:
                return False
        return True

    return False
