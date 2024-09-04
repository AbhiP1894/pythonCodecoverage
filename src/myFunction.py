import os

def Sum(number1, number2):
    return number1 + number2

def Random(number):
    # Convert the byte result of urandom to a string using decode('latin1')
    return '%d%s' % (number, os.urandom(number).decode('latin1'))
