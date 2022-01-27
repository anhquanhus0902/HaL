class Node:
        
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        '''
        Các thao tác trên cây nhị phân sẽ được thực hiện thông qua tham chiếu tới
        nút gốc root
        '''
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def addNode(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.put(self.root, data)
    
    def put(self, currentNode, data):
        if data < currentNode.val:
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self.put(currentNode.left, data)
        else:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self.put(currentNode.right, data)
    
    def buildTreeFromList(self,datas): 
        for i in datas:
            self.addNode(i)
        
    def search(self, val):
        return self._search(self.root, val)
            
    def _search(self, currentNode, val):
        if currentNode is None:
            return False
        else:
            if val < currentNode.val:
                return self._search(currentNode.left, val)
            elif val > currentNode.val:
                return self._search(currentNode.right, val)
            else:
                return True

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, currentNode):
        if not currentNode is None:
            return [currentNode.val] + self._preOrder(currentNode.left) + self._preOrder(currentNode.right)
        else:
            return []

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):
        if not currentNode is None:
            return self._inOrder(currentNode.left) + [currentNode.val] + self._inOrder(currentNode.right)
        else:
            return []
 
    def postOrder(self):
        return self._postOrder(self.root)
    
    def _postOrder(self, currentNode):
        if not currentNode is None:
            return self._postOrder(currentNode.left) + self._postOrder(currentNode.right) + [currentNode.val]
        else:
            return []
      
    def getHeight(self):
        return self._getHeight(self.root)-1

    def _getHeight(self, currentNode):
        if currentNode is None:
            return 0
        else:
            leftHeight = self._getHeight(currentNode.left)
            rightHeight = self._getHeight(currentNode.right)
            return max(leftHeight, rightHeight) + 1
    
    def getSumLeftChild(self, node):
        return self.getSum(node.left)
    
    def getSumRightChild(self, node):
        return self.getSum(node.right)
   
    def getSum(self, node):
        if node is None:
            return 0
        else:
            return node.val + self.getSum(node.left) + self.getSum(node.right)

    def getTilt(self):
        return self._getTilt(self.root)
    
    def _getTilt(self, currentNode):
        if currentNode is None:
            return 0
        else:
            return abs(self.getSumLeftChild(currentNode) - self.getSumRightChild(currentNode)) + self._getTilt(currentNode.left) + self._getTilt(currentNode.right)

# Những dòng dưới đây là code chạy thử chương trình, sinh viên không cần chỉnh sửa

if __name__ == '__main__':
    
    bst = BinarySearchTree()
    
    datas = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
    
    bst.buildTreeFromList(datas)
    
    print('Search 7:',bst.search(7))
    print('Search 12:',bst.search(12))
    
    print('PreOrder:',bst.preOrder())
    print('InOrder:',bst.inOrder())
    print('PostOrder:',bst.postOrder())
    print('Get height:',bst.getHeight())
    print('Sum of left child tree:',bst.getSumLeftChild(bst.getRoot()))
    print('Sum of right child tree:',bst.getSumRightChild(bst.getRoot()))
    print('Tilt of tree:',int(bst.getTilt()))