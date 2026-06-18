import re

from utils import convertToNumber, isEmpty, isNumOrDot, isValidNumber

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.fullmatch(string))

# backward compatibility
def inNumOrDot(string: str):
    return isNumOrDot(string)


def convertToNumber(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number

# backward compatibility
def converToNumber(string: str):
    return convertToNumber(string)

def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

def isEmpty(string: str):
    return len(string) == 0

