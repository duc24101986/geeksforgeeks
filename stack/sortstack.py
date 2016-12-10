from stack import Stack

def sortStack(stack):
    if not(stack.isEmpty()):
        temp = stack.pop()
        sortStack(stack)
        sortInsert(stack, temp)
        
def sortInsert(stack, temp):
    if stack.isEmpty() or stack.peek()<temp:
        stack.push(temp)
    else:
        temp2 = stack.pop()
        sortInsert(stack, temp)
        stack.push(temp2)
        
if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(20)
    stack.push(10)
    stack.push(50)
    print 'Original stack'
    stack.traverse()
    sortStack(stack)
    print 'Sorted stack'
    stack.traverse()