from moving_utils import *
from farm_utils import *

def sunflowerDrones(args):
	drones = []
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]
	
	for i in range(startX + 1, endX + 1):
		drones.append({
			"mainDrone": False,
			"args": {
				"startX": i,
				"startY": startY,
				"endX": i,
				"endY": endY
			}
		})
	drones.append({
		"mainDrone": True,
		"args": {
			"startX": startX,
			"startY": startY,
			"endX": startX,
			"endY": endY
		}
	})
	
	return drones

def plantSunflower(args):
	change_hat(Hats.Golden_Cactus_Hat)
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]
	
	for x in range(startX, endX + 1):
		for y in range(startY, endY + 1):
			goTo(x, y)
			if checkGroundAndHarvest(Entities.Sunflower) == -1:
				return

	for currHighest in range(15, 7 - 1, -1):
		for x in range(startX, endX + 1):
			for y in range(startY, endY + 1):
				goTo(x, y)
				if measure() == currHighest:
					while not checkGroundAndHarvest(Entities.Sunflower, False):
						pass
				
def main():
	N = get_world_size() - 1
	plantSunflower({
		"startX": N - 8,
		"startY": 0,
		"endX": N,
		"endY": 11
	})

if __name__ == "__main__":
	main()