# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.link = deque()
        self.notSearch = True

    def getValue(self):
        if self.notSearch:
            self.notSearch = False
            return self.value
        else:
            return None

    def addLink(self, node):
        start = 0
        end = len(self.link)-1
        while start<end:
            half = (start+end)//2
            if self.link[half].value>node.value:
                end = half-1
            elif self.link[half].value<node.value:
                start = half+1
        if len(self.link)==0:
            self.link.append(node)
        elif self.link[start].value<node.value:
            self.link.insert(start+1, node)
        else:
            self.link.insert(start, node)
    
    def getLink(self):
        return self.link.copy()
    
    def reset(self):
        self.notSearch = True


(N, M, V) = list(map(int, input().split()))
Nodes = [Node(i+1) for i in range(N)]

# save
for i in range(M):
    (_v1, _v2) = list(map(int, input().split()))
    Nodes[_v1-1].addLink(Nodes[_v2-1])
    Nodes[_v2-1].addLink(Nodes[_v1-1])

# DFS
stack = deque([Nodes[V-1]])
s = []
while len(stack)!=0:
    node = stack.popleft()
    if node.notSearch:
        s.append(str(node.getValue()))
        link = node.getLink()
        while len(link)!=0:
            stack.appendleft(link.pop())
print(' '.join(s))

for i in range(N):
    Nodes[i].reset()

# BFS
stack = deque([Nodes[V-1]])
s = []
while len(stack)!=0:
    node = stack.popleft()
    if node.notSearch:
        s.append(str(node.getValue()))
        link = node.getLink()
        while len(link)!=0:
            stack.append(link.popleft())
print(' '.join(s))
