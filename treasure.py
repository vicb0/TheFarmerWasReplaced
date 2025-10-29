from moving_utils import *
from farm_utils import *

dirs = {(1, 0): East, (-1, 0): West, (0, 1): South, (0, -1): North}
opposite = {East: West, West: East, North: South, South: North}

def treasureDrones(args):
	return [{
		"mainDrone": True,
		"args": args
	}]

def convertYCoord(yCoord):
	N = get_world_size() - 1
	return N - yCoord

def setupGridMatrix():
	N = get_world_size()
	matrix = []
	
	for i in range(N):
		row = []
		for j in range(N):
			row.append({North: -1, South: -1, East: -1, West: -1})
		matrix.append(row)
	
	return matrix

def mapping():
	N = get_world_size() - 1
	map = setupGridMatrix()

	def dfsAll(lastDir=None):
		currPosX, currPosY = get_pos_x(), get_pos_y()
		currPosY = convertYCoord(currPosY)

		for dir in dirs:
			newPosX, newPosY = currPosX + dir[0], currPosY + dir[1]
			if not (0 <= newPosX <= N and 0 <= newPosY <= N):
				continue
			if not can_move(dirs[dir]):
				map[currPosY][currPosX][dirs[dir]] = 0
				continue
			if map[currPosY][currPosX][dirs[dir]] != -1:
				continue
			map[newPosY][newPosX][opposite[dirs[dir]]] = 1
			map[currPosY][currPosX][dirs[dir]] = 1
			move(dirs[dir])
			dfsAll(dirs[dir])
		
		if lastDir != None:
			move(opposite[lastDir])

	dfsAll()
	return map	

def orderDirs(currPos, goalCoords):
	dx = goalCoords[0] - currPos[0]
	dy = goalCoords[1] - currPos[1]
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
	return bestDirs

def dfsIterative(map, treasureCoords):
	queue = [((get_pos_x(), convertYCoord(get_pos_y())), ())]
	visited = set()
	
	while len(queue) > 0:
		currPos, path = queue.pop()
		
		if currPos == treasureCoords:
			return path

		visited.add(currPos)
		bestDirs = orderDirs(currPos, treasureCoords)
		
		for i in range(len(bestDirs) - 1, -1, -1):
			dir = bestDirs[i]
			newPos = (currPos[0] + dir[0], currPos[1] + dir[1])
			if map[currPos[1]][currPos[0]][dirs[dir]] != 1:
				continue
			if newPos in visited:
				continue
			queue.append((newPos, path + (dirs[dir],)))

def solveMaze(args):
	N = get_world_size()
	weirdSubstanceCost = N * 2**(num_unlocked(Unlocks.Mazes) - 1)
	change_hat(Hats.Golden_Cactus_Hat)

	goTo(0, 0)
	checkGroundAndHarvest(Entities.Bush)
	use_item(Items.Weird_Substance, weirdSubstanceCost)

	c = 0
	map = mapping()

	while c <= 300 and num_items(Items.Weird_Substance) >= weirdSubstanceCost:
		treasureX, treasureY = measure()		
		path = dfsIterative(
			map,
			(treasureX, convertYCoord(treasureY))
		)

		for mov in path:
			currPosX = get_pos_x()
			currPosY = convertYCoord(get_pos_y())
			for dir in dirs:
				if can_move(dirs[dir]):
					map[currPosY][currPosX][dirs[dir]] = 1
				else:
					map[currPosY][currPosX][dirs[dir]] = 0
			move(mov)

		use_item(Items.Weird_Substance, weirdSubstanceCost)		
		c += 1
	harvest()

def main():
#	clear()
#	set_world_size(4)
	N = get_world_size() - 1
	solveMaze({})
	
if __name__ == "__main__":
	main()