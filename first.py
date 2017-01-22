def sum(numberOne, numberTwo):
    numberOneInt = convertInteger(numberOne)
    numberTwoInt = convertInteger(numberTwo)
    
    result = numberOneInt + numberTwoInt
    
    return result

def convertInteger(numberString):
    convertedInteger = int(numberString)
    return convertedInteger

answer = sum("1","2")
    