# N과 M (1)
from collections import deque

class node:
    def __init__(self, data, next=None):
        
stack = deque()
queue= deque()

(N, M) = list(map(int, input().split(' ')))
