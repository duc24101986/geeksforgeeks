from stack import Stack 

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
    # out put postfix
    strPostFix = ''
    
    # stack to store the operator
    stackOperator = Stack()
    
    for c in strInFix:
        if c.isdigit(): # if character is a digit
            strPostFix += c
        elif isOperator(c): # if character is operator
            if stackOperator.isEmpty():
                stackOperator.push(c)
            elif (calPriority(c) > calPriority(stackOperator.peek())):
                stackOperator.push(c)
            else:
                strPostFix += stackOperator.pop()
                stackOperator.push(c)
        elif c == '(':
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
    for c in strPostFix:
        if c.isdigit():
            stackOperand.push(c)
        elif isOperator(c):
            operand1 = int(stackOperand.pop())
            operand2 = int(stackOperand.pop())
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
    strPostFix = convertInfix2Postfix('12+2+3+4+5')
    print strPostFix
    # print calPostFix(strPostFix)