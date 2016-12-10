from stack import Stack
import math

'''
Author: Pham Minh Duc
Date  : 14/08/2016

This is the math parser based on shunting yard algorithm
    + Input a math statement. The operation support: + , -, *, / and function sin, cos, tan, atan, power(a, b)
    + Convert to postfix format
    + Evaluate the postfix 
Reference: https://en.wikipedia.org/wiki/Shunting-yard_algorithm
'''

class MathParser():
    def __init__(self):
        self.token = []
        self.strPostFix = []
        self.FUNCTION = ['sin', 'cos', 'tan', 'atan', 'pow']
        self.functionTable = {'sin': math.sin, 'cos': math.cos, 'tan':math.tan, 'atan':math.atan, 'pow': math.pow }
        self.funcArgLenth  = {'sin': 1,        'cos': 1,        'tan':1,        'atan':1,         'pow': 2        }
        self.OPERATOR = ['+', '-', '*', '/']
        self.OPERATOR_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    def isOperand(self, c):
        if isinstance(c, float):
            return True
        else:
            return False
        
    def isOperator(self,c):
        if c in self.OPERATOR:
            return True
        else:
            return False
    
    def isParenthese(self, c):
        return c=='(' or c==')'
        
    def isFunction(self, func):
        if func in self.FUNCTION:
            return True
        else:
            return False
    
    def isFunctionSeparator(self, c):
        if c ==',':
            return True
        else:
            return False
        
    def calPriority(self,c):
        if self.isOperator(c):
            return self.OPERATOR_PRIORITY[c]
    
    def convertToken(self, strInput):
        # Convert to token string
        # Operator: '+, -, *, /'
        # Operand: real number
        # Parenthese ( )
        # Space ' '
        # Function: 'sin, cos, tan'
        # separator ','
        
        # Remove all the space first
        strStatement = ''
        for c in strInput:
            if c != ' ':
                strStatement+=c
    
        # Parse each element in the string.
        operand = ''
        function = ''
        index = 0
        for c in strStatement:
            index += 1
            if c.isdigit() or c =='.':
                operand +=c
                if index < len(strStatement):
                    if (strStatement[index] == ')' or self.isOperator(strStatement[index]) or self.isFunctionSeparator(strStatement[index])):
                        self.token.append(float(operand))
                        operand = ''
    
                elif index == len(strStatement):
                    self.token.append(float(operand))
                    operand = ''
                    
            elif self.isOperator(c) or self.isParenthese(c):
                self.token.append(c)
            
            elif self.isFunctionSeparator(c):
                self.token.append(c)
                
            elif c.isalpha() and (self.isFunctionSeparator(c)==False):
                function +=c
                if strStatement[index] == '(':
                    self.token.append(function)
                    function=''
    
    def validateToken(self):
        isTokenValid = True
        for t in self.token:
            if self.isFunction(t) or self.isOperator(t) or self.isParenthese(t) or isinstance(t, float):
                isTokenValid = True
            else:
                isTokenValid = False
                print t + ' is invalid token'
                return isTokenValid
        return isTokenValid
    
    def convertInfix2Postfix(self):
        # out put postfix
        strPostFix = []
        index = 0
        # stack to store the operator
        stackOperator = Stack()
        
        for c in self.token:
            index += 1
            
            #Scan the number
            if self.isOperand(c):
                strPostFix.append(c)    
                
            # Scan function
            elif self.isFunction(c):
                stackOperator.push(c)
            
            # Scan function argument separator
            elif self.isFunctionSeparator(c):
                while stackOperator.peek() != '(':
                    strPostFix.append(stackOperator.pop())
                
            # Scan operator
            elif self.isOperator(c): # if character is operator
                if stackOperator.isEmpty():
                    stackOperator.push(c)
                elif (self.calPriority(c) > self.calPriority(stackOperator.peek())):
                    stackOperator.push(c)
                else:
                    strPostFix += stackOperator.pop()
                    stackOperator.push(c)
            
            # scan the open parentheses
            elif c == '(': 
                    stackOperator.push(c)
                    
            # scan the closed parentheses
            elif c == ')':
                status = True
                while status:
                    if (stackOperator.peek() == '('):
                        status = False
                        stackOperator.pop() # Pop the (
                    else:
                        status = True
                        strPostFix.append(stackOperator.pop())
                
                # if the next element is function then pop it
                if (stackOperator.isEmpty()==False) :
                    if self.isFunction(stackOperator.peek()):
                        strPostFix.append(stackOperator.pop())
                    
            else:
                print "In valid input"
                return
    
        while not(stackOperator.isEmpty()):
            strPostFix.append(stackOperator.pop()) 
        
        self.strPostFix = strPostFix
        
    def calPostFix(self):
        stackOperand = Stack()
  
        for c in self.strPostFix:
            if self.isOperand(c):
                stackOperand.push(c)
            
            elif self.isFunction(c):
                argLength = self.funcArgLenth[c]
                if argLength == 1:
                    operand1 = stackOperand.pop()
                    result = self.functionTable[c](operand1)
                elif argLength == 2: 
                    operand2 = stackOperand.pop()
                    operand1 = stackOperand.pop()
                    result = self.functionTable[c](operand1, operand2)
                stackOperand.push(result) 
                
            elif self.isOperator(c):
                operand1 = stackOperand.pop()
                operand2 = stackOperand.pop()
                if c == '+':
                    result = operand1 + operand2
                elif c == '-':
                    result = operand1 - operand2
                elif c == '*':
                    result = operand1 * operand2
                elif c == '/':
                    result = operand1 / operand2
                    
                stackOperand.push(result)    
        
        return stackOperand.pop()

# Test function
if __name__ == '__main__':
    calculator = MathParser()
    
    isContinue = True
    
    while isContinue == True:
        default = '<mathparser>:'
        statement = raw_input(default)
        
        if statement == 'stop':
            isContinue = False
        else:
            calculator.convertToken(statement)
            print calculator.token
            calculator.convertInfix2Postfix()
            print calculator.strPostFix
            print calculator.calPostFix()