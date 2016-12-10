from stack import Stack

## This is calculator implementation
# Operator + - * / 
# Operator priority:
# 
# * / : 2
# + - : 1
# Parenthese ()
# Operand real number 0.345
# input is the string of calulation, 0.567*4.678-12345/345.678 =
# output is the results

def isOperator(c):
    OPERATOR = ['+', '-', '*', '/']
    if c in OPERATOR:
        return True
    else:
        return False
        
def calPriority(c):
    OPERATOR_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}
    if isOperator(c):
        return OPERATOR_PRIORITY[c]
    
def convertInfix2Postfix(strInFix):
    operand = ''
    # out put postfix
    strPostFix = ''
    index = 0
    # stack to store the operator
    stackOperator = Stack()
    
    for c in strInFix:
        index += 1
        if (c.isdigit() or (c=='.')): # if character is a digit
            operand +=c
            if index < len(strInFix):
                if (strInFix[index] == ')' or isOperator(strInFix[index])):
                    strPostFix += operand
                    strPostFix += '_' # add this to separate the operand
                    operand = ''

            elif index == len(strInFix):
                strPostFix += operand
                strPostFix += '_' # add this to separate the operand
                operand = ''
                
        # Scan operator
        elif isOperator(c): # if character is operator
            if stackOperator.isEmpty():
                stackOperator.push(c)
            elif (calPriority(c) > calPriority(stackOperator.peek())):
                stackOperator.push(c)
            else:
                strPostFix += stackOperator.pop()
                stackOperator.push(c)
        
        elif c == '(': # scan the parentheses
                stackOperator.push(c)
        elif c == ')':
            status = True
            while status:
                if (stackOperator.peek() == '('):
                    status = False
                    stackOperator.pop() # Pop the (
                else:
                    status = True
                    strPostFix += stackOperator.pop()
            
        else:
            print "In valid input"
            return

    while not(stackOperator.isEmpty()):
        strPostFix += stackOperator.pop()        
    
    return strPostFix

def calPostFix(strPostFix):
    stackOperand = Stack()
    operand = ''
    for c in strPostFix:
        if (c.isdigit() or (c == '.')):
            operand += c
        elif c == '_':
            stackOperand.push(float(operand))
            operand = ''
        elif isOperator(c):
            operand1 = float(stackOperand.pop())
            operand2 = float(stackOperand.pop())
            if c == '+':
                result = operand1 + operand2
            elif c == '-':
                result = operand1 - operand2
            elif c == '*':
                result = operand1 * operand2
            elif c == '/':
                result = operand1 / operand2
                
            stackOperand.push(str(result))    
    
    return stackOperand.pop()

if __name__ == '__main__':
    strPostFix = ''
    strPostFix = convertInfix2Postfix('(2.5+4.6)*(7.5+3.5)+4.3*2.0')
    print strPostFix
    print calPostFix(strPostFix)