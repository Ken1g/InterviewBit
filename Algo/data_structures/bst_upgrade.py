class Node:
    def __init__(self, val, name):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.name = name
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
        
    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children
        
class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val, name):
        self.root = Node(val, name)

    def insert(self, val, name):
        if (self.root is None):
            self.setRoot(val, name)
        else:
            self.insertNode(self.root, val, name)

    def insertNode(self, currentNode, val, name):
        if (val <= currentNode.val):
            if (currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val, name)
            else:
                currentNode.leftChild = Node(val, name)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val, name)
            else:
                currentNode.rightChild = Node(val, name)

    def find(self, val, name):
        return self.findNode(self.root, val, name)

    def findNode(self, currentNode, val, name):
        if (currentNode is None):
            return False
        elif (val == currentNode.val):
            if name == currentNode.name:
                return True
            else:
                return self.findNode(currentNode.leftChild, val, name) 
        elif (val < currentNode.val):
            return self.findNode(currentNode.leftChild, val, name)
        else:
            return self.findNode(currentNode.rightChild, val, name)

tree = BST()
tree.setRoot(10, "wow")
tree.insert(11, "wwq")
tree.insert(12, "wwrwe")
tree.insert(12, "reg")
tree.insert(12, "wwrwee")
tree.insert(12, "reg")
print(tree.find(12, "wwrwee"))
#print(tree.find(9, "ewr"))
