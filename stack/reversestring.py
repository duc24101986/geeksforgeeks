from stack import Stack

def reverseString(strOriginal):
    stack_ = Stack()
    strReverse = ''
    for c in strOriginal:
        stack_.push(c)
    
    status = True
    while status:
        if stack_.size() == 0:
            status = False
        else:
            strReverse += stack_.pop()
            status = True
    
    return strReverse

if __name__ == '__main__':
    strOriginal = 'ABCDEFGHIJKLMN0123456789'
    print reverseString(strOriginal)
        