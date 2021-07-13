# 2048 (Easy)

import sys
import copy

N = int(input())
board = [list(map(int, input().split())) for n in range(N)]

def up():
	global N
	save = [[True for n in range(N)] for m in range(N)]
	for y in range(N):
		for x in range(N):
			if board[y][x]==0:
				continue
			_y = y-1
			while _y>=0:
				if board[_y][x]==0:
					_y -= 1
				elif save[_y][x] and board[_y][x]==board[y][x]:
					board[y][x] *= 2
					save[_y][x] = False
					_y -= 1
					break
				else:
					break
			temp = board[y][x]
			board[y][x] = 0
			board[_y+1][x] = temp
	return max([max(board[n]) for n in range(N)])

def down():
	global N
	board.reverse()
	up()
	board.reverse()
	return max([max(board[n]) for n in range(N)])
	
def left():
	global N
	save = [[True for n in range(N)] for m in range(N)]
	for y in range(N):
		for x in range(N):
			if board[y][x]==0:
				continue
			_x = x-1
			while _x>=0:
				if board[y][_x]==0:
					_x -= 1
				elif save[y][_x] and board[y][_x]==board[y][x]:
					board[y][x] *= 2
					save[y][_x] = False
					_x -= 1
					break
				else:
					break
			temp = board[y][x]
			board[y][x] = 0
			board[y][_x+1] = temp
	return max([max(board[n]) for n in range(N)])
	
def right():
	global N
	for n in range(N):
		board[n].reverse()
	left()
	for n in range(N):
		board[n].reverse()
	return max([max(board[n]) for n in range(N)])
	
def dp(n, m):
	global board
	if n==5:
		return m
	_max = m
	save_board = copy.deepcopy(board)
	_max = max(_max, dp(n+1, up()))
	board = copy.deepcopy(save_board)
	_max = max(_max, dp(n+1, down()))
	board = copy.deepcopy(save_board)
	_max = max(_max, dp(n+1, left()))
	board = copy.deepcopy(save_board)
	_max = max(_max, dp(n+1, right()))
	board = copy.deepcopy(save_board)
	return _max
		
_max = max([max(board[n]) for n in range(N)])
print(dp(0, _max))
