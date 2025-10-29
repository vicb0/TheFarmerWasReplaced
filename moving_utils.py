def isInRectEdge(currPos, rect):
	return (currPos[0] == rect[0] or
		currPos[1] == rect[1] or
		currPos[0] == rect[2] or
		currPos[1] == rect[3])

def moveN(dir, n):
	for i in range(n):
		if not move(dir):
			return False
	return True

def goTo(destX, destY):
	N = get_world_size()
	startX, startY = get_pos_x(), get_pos_y()
	stuck = False
	
	if abs(destY - startY) < N - abs(destY - startY):
		if destY < startY:
			stuck = not moveN(South, abs(destY - startY))
		else:
			stuck = not moveN(North, abs(destY - startY))
	else:
		if destY < startY:
			stuck = not moveN(North, N - abs(startY - destY))
		else:
			stuck = not moveN(South, N - abs(startY - destY))
	
	if stuck:
		return False
	
	if abs(destX - startX) < N - abs(destX - startX):
		if destX < startX:
			stuck = not moveN(West, abs(destX - startX))
		else:
			stuck = not moveN(East, abs(destX - startX))
	else:
		if destX < startX:
			stuck = not moveN(East, N - abs(startX - destX))
		else:
			stuck = not moveN(West, N - abs(startX - destX))
			
	return stuck

def traverseRect(startX, startY, endX, endY):
	x, y = get_pos_x(), get_pos_y()

	if (y - startY) % 2 == 0:
		if x == endX:
			if y == endY:
				return True
			move(North)
			return False
		move(East)
	else:
		if x == startX:
			if y == endY:
				return True
			move(North)
			return False
		move(West)
	
	return False

def buildPath(instructions):
	path = []

	for (dir, n) in instructions:
		for _ in range(n):
			path.append(dir)
		
	return path
	
def main():
	sx, sy, ex, ey = 3, 4, 8, 6
	goTo(0,0)
	
if __name__ == "__main__":
	main()