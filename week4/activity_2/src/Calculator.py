def add(num1, num2):
    '''

    :param num1: first number
    :param num2: second number
    :return: 2 numbers added
    '''
    if type(num1) or type(num2) in [complex]:
        return num1 + num2
    elif type(num1) or type(num2) not in [int, float]:
        raise TypeError("The numbers must be integers or floats")


    return num1 + num2

# result = add(1, )
# print(result)