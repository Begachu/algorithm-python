# 최대 힙
import sys
input = sys.stdin.readline

N = int(input())
root = None

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.length = 1

    def addNode(self, node):
        if node.value>self.value:
            if self.left==None:
                self.left = node
            else:
                self.left.addNode(node)
        elif node.value<self.value:
            if self.right==None:
                self.right = node
            else:
                self.right.addNode(node)
        self.length += 1

    def findMax(self):
        left = self
        while self.left != None and self.left.left != None:
            left = self.left.findMax()
        return left
        
    def removeNode(self, value):
        global root
        if value==self.value:
            pop = self.value
            if self.left != None:
                temp = self.findMax()
                self.value = temp.left.value
                temp.left = None
            elif self.right != None:
                root = self.right
            else:
                root = None
            self.length -= 1
            return pop

        elif value>self.value:
            if self.left == None:
                return None
            else:
                result = self.left.removeNode(value)
                if result != None:
                    self.length -= 1
                    return result
        elif value<self.value:
            if self.right == None:
                return None
            else:
                result = self.right.removeNode(value)
                if result != None:
                    self.right -= 1
                    return result
        return None

    def popNode(self):
        global root
        if self.left == None:
            pop = self.value
            if self.right == None:
                root = None
            else:
                root = self.right
            return pop
        temp = self.findMax()
        pop = temp.left.value
        temp.left = None
        return pop
    
for n in range(N):
    _input = int(input())
    if _input==0:
        if root == None:
            print(0)
        else:
            print(root.popNode())
    else:
        if root==None:
            root = Node(_input)
        else:
            root.addNode(Node(_input))
        