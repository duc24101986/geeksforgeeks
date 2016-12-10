# Create a link list
class LinkList:
    def __init__(self):
        self.head = None
    
    def insertNode(self, value):
        node = Node(value)
        if (self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def traverseNode(self):
        temp = self.head
        while (temp):
            print temp.data
            temp = temp.next
            

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
if __name__ == '__main__':
    linkList = LinkList()
    linkList.insertNode(1)
    linkList.insertNode(2)
    linkList.insertNode(3)
    linkList.insertNode(4)
    linkList.insertNode(5)
    linkList.insertNode(6)
    linkList.traverseNode()
    
    a = {'data': 6}
    print a['data']