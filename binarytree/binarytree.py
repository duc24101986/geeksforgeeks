

'''
Binary tree is a tree where each node has only 2 child, no order
It is differrent from BST where BST has order such that the lef child < root < right value
'''

from stack.stack import Stack

class Node():
    def __init__(self, rootkey):
        self.key = rootkey
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, leftkey):
        if self.leftChild == None:
            self.leftChild = Node(leftkey)
        else:
            newNode = Node(leftkey)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode
        
    def insertRight(self, rightkey):
        if self.rightChild == None:
            self.rightChild = Node(rightkey)
        else:
            newNode = Node(rightkey)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
        
    def setRootValue(self, key):
        self.key = key
        
    def getRootValue(self):
        return self.key

def parseMath(strMath):
    '''
        ( : create new left node and move to it
        number: set the current node, and move to parent
        operator : set the current node, create right node and move there
        ) : move to parent
    '''
    listMath = strMath.split()
    stackParentNode = Stack()
    
    binaryTree = Node('')
    currentNode = binaryTree
    
    for c in listMath:
        if c == '(':
            binaryTree.insertLeft('')
            stackParentNode.push(currentNode)
            currentNode = binaryTree.getLeftChild()
        elif c not in ['+', '-', '*', '/', ')']:
            currentNode.setRootValue(int(c))
            currentNode = stackParentNode.pop()
        elif c in ['+', '-', '*', '/']:
            currentNode.setRootValue(c)
            currentNode.insertRight('')
            stackParentNode.push(currentNode)
            currentNode = currentNode.getRightChild()
        elif c == ')':
            currentNode = stackParentNode.pop()
    
    
    

    
        