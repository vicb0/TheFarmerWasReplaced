from moving_utils import *
from farm_utils import *

def weirdSubstanceDrones(args):
	N = get_world_size() - 1
	startX = args["startX"]
	startY = args["startY"]

	drones = []

	for i in range(3, N, 7):
		for j in range(3, N, 7):
			if (i, j) == (startX, startY):
				continue
			drones.append({
				"mainDrone": False,
				"args": {
					"startX": j,
					"startY": i
				}
			})

	drones.append({
		"mainDrone": True,
		"args": {
			"startX": startX,
			"startY": startY
		}
	})

	return drones			

def farmWeirdSubstance(args):
	startX = args["startX"]
	startY = args["startY"]
	
	change_hat(Hats.Golden_Cactus_Hat)
	goTo(startX, startY)
	checkGroundAndHarvest(Entities.Tree)
	use_item(Items.Fertilizer)
	compPlant, (compX, compY) = get_companion()
	goTo(compX, compY)
	checkGroundAndHarvest(compPlant)
	goTo(startX, startY)

def main():
	farmWeirdSubstance({
		"startX": 3,
		"startY": 3,
		"endX": 3,
		"endY": 3
	})
	
if __name__ == "__main__":
	main()