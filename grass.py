from moving_utils import *
from farm_utils import *

def grassDrones(args):
	drones = []
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]
	N = get_world_size() - 1
	
	for i in range(3, N, 14):
		for j in range(3, N, 14):
			if (i, j) == (startX, startY):
				continue
			drones.append({
				"mainDrone": False,
				"args": {
					"startX": i,
					"startY": j,
					"endX": i + 7,
					"endY": j + 7
				}
			})
	drones.append({
		"mainDrone": True,
		"args": {
			"startX": startX,
			"startY": startY,
			"endX": endX,
			"endY": endY
		}
	})
	
	return drones

def plantGrass(args):
	change_hat(Hats.Golden_Cactus_Hat)
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]

	path = buildPath([
		(North, abs(endY - startY)),
		(East, abs(endX - startX)),
		(South, abs(endY - startY)),
		(West, abs(endX - startX)),
	])

	goTo(startX, startY)
	companions = {}
	for dir in path:
		checkGround(Grounds.Grassland)
		isInRect, isOccupied = True, True
		while isInRect or isOccupied:
			replant(Entities.Grass)
			plantType, coords = getCompanion()
			isInRect = isInRectEdge(coords, (startX, startY, endX, endY))
			isOccupied = coords in companions
		companions[coords] = plantType
		def split():
			goTo(coords[0], coords[1])
			checkGroundAndHarvest(companions[coords])
		spawn_drone(split)
		move(dir)
			
def main():
	plantGrass({
		"startX": 3,
		"startY": 3,
		"endX": 10,
		"endY": 10
	})

if __name__ == "__main__":
	main()