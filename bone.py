from moving_utils import *
from farm_utils import *

start = get_time()
TIME_LIMIT = 5
dirs = {(1, 0): East, (-1, 0): West, (0, 1): North, (0, -1): South}

def boneDrones(args):
	return [{
		"mainDrone": True,
		"args": args
	}]

def dfs(snakeTiles, applePos, visited, lastDir=None):
	if get_time() - start >= TIME_LIMIT:
		return None
		 
	currPos = snakeTiles[0]
	if currPos == applePos:
		return []
	
	N = get_world_size()
	dx = applePos[0] - currPos[0]
	dy = applePos[1] - currPos[1]

	bestDirs = []
	for d in dirs:
		score = dx * d[0] + dy * d[1]
	
		inserted = False
		for i in range(len(bestDirs)):
			other = bestDirs[i]
			otherScore = dx * other[0] + dy * other[1]
			if score > otherScore:
				bestDirs.insert(i, d)
				inserted = True
				break
		if not inserted:
			bestDirs.append(d)
		
	for dir in bestDirs:
		dx, dy = dir
		newPos = (currPos[0] + dx, currPos[1] + dy)
	
		if not (0 <= newPos[0] < N and 0 <= newPos[1] < N):
			continue 
		if ((lastDir, dirs[dir]) in ((West, East), (East, West)) or
			(lastDir, dirs[dir]) in ((North, South), (South, North))
		):
			continue
		if newPos in snakeTiles or newPos in visited:
			continue
		visited.add(newPos)
		res = dfs((newPos,) + snakeTiles[:-1], applePos, visited, dirs[dir])
		if res != None:
			direction = dirs[dir] 
			return [direction] + res

	return None

def snakeGamePathfind(args):
	global start
	global TIME_LIMIT
	
	start = get_time()
	TIME_LIMIT = args["timeLimit"]
	
	clear()
	change_hat(Hats.Dinosaur_Hat)
	
	currPos = (get_pos_x(), get_pos_y())
	snake = currPos
	path = dfs((currPos, currPos), measure(), set())
	while path != None and len(path) > 0:
		c = 0
		for dir in path:
			move(dir)
			currPos = (get_pos_x(), get_pos_y())
			if c == 0:
				snake = (currPos,) + snake
			else:
				snake = (currPos,) + snake[:-1]
			c += 1
		start = get_time()
		path = dfs(snake, measure(), set(), path[-1])
	change_hat(Hats.Sunflower_Hat)
		
def snakeGameBruteForce(args):
	clear()
	change_hat(Hats.Dinosaur_Hat)
	N = get_world_size()

	def L2R(appleY):
		path = []
		y = get_pos_y()
		for _ in range(max(y - appleY, 1)):
			path.append(South)
		for _ in range(N - 1):
			path.append(East)
		return path
		
	def R2L(appleY):
		path = []
		y = get_pos_y()
		for _ in range(max(appleY - y, 1)):
			path.append(North)
		for _ in range(N - 1):
			path.append(West)
		return path

	tail = 0
	appleX, appleY = measure()
	while tail < N * 2 - 1:
		for dir in L2R(appleY):
			move(dir)
			if measure() != None:
				appleX, appleY = measure()
				tail += 1
		for dir in R2L(appleY):
			move(dir)
			if measure() != None:
				appleX, appleY = measure()
				tail += 1
	
	for _ in range(get_pos_y()):
		move(South)

	N = get_world_size() - 1
	while True:
		completed = False
		while not completed:
			before = (get_pos_x(), get_pos_y())
			completed = traverseRect(1, 0, N, N)
			if (get_pos_x(), get_pos_y()) == before:
				break
		move(West)
		for _ in range(N):
			move(South)
		if not move(East):
			break
	change_hat(Hats.Sunflower_Hat)

def snakeGame(args):
	snakeGameBruteForce(args)

def main():
	N = get_world_size() - 1
	snakeGame({
		"startX": 0,
		"startY": 0,
		"endX": N,
		"endY": N,
		"timeLimit": 7.5
	})

if __name__ == "__main__":
	main()