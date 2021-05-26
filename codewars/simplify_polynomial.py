import re

def simplify(poly):

    obj = {}
    monomials = re.split('\+|\-', poly)
    preOps = re.split('[0-9]*[a-z]*[a-z]*', poly)
    operators = []

    for item in preOps:
        if len(item) > 0:
            operators.append(item)
    
    if len(monomials[0]) == 0:
        monomials.pop(0)
        pass
    else:
        operators.insert(0, '+')
        pass
    
    for i in range (len(monomials)):
        obj[i] = {
            'coeff': '',
            'vars': '',
            'opr': ''
        }

    for i in range(len(monomials)):
        for j in range(len(monomials[i])):
            if monomials[i][j].isdigit():
                obj[i]['coeff'] += monomials[i][j]
            else:
                obj[i]['vars'] += monomials[i][j]
        obj[i]['opr'] = operators[i]

    for item in obj:
        if len(obj[item]['coeff']) == 0:
            obj[item]['coeff'] = '1'
        obj[item]['vars'] = ''.join(sorted(obj[item]['vars']))
    
    """
    At this point, we have an object containing all monomials with their coefficients, variables (alphabetized), and operators. 
    Next we need to add similar monomials together. 
    Then we need to organize in order of increasing num of variables.
    Then we need to organize similar num of variables in lexicographic order.
    """


    for item in obj:
        print(obj[item])


simplify("-32344a+5acdefb+3a-c-2xa")

