class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        length = len(self.items) - 1
        return self.items[length]
    
    def size(self):
        return len(self.items)
        
    def isEmpty(self):
        return self.items == []
    
    def traverse(self):
        for i in list(reversed(range(len(self.items)))):
            print '[' + str(i) + ']' + ' -> ' + str(self.items[i])


if __name__ == '__main__':
    stack = Stack()
    for i in range(1000):
        stack.push(i)

    print "length : " + str(stack.size())
    stack.traverse()
    
