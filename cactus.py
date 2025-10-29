from moving_utils import *
from farm_utils import *

def cactusDrones(args):
	drones = []
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]
	
	for i in range(startY + 1, endY + 1):
		drones.append({
			"mainDrone": False,
			"args": {
				"validator": False,
				"startX": startX,
				"startY": i,
				"endX": endX,
				"endY": i
			}
		})
	drones.append({
		"mainDrone": True,
		"args": {
			"validator": True,
			"topY": endY,
			"startX": startX,
			"startY": startY,
			"endX": endX,
			"endY": startY
		}
	})
	
	return drones

def plantCactusSort(args):
	change_hat(Hats.Golden_Cactus_Hat)
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]

	for y in range(startY, endY + 1):
		for x in range(startX, endX + 1):
			goTo(x, y)
			if checkGroundAndHarvest(Entities.Cactus) == -1:
				return

			while True:
				left_bigger = (measure(West) != None and measure(West) > measure())
				down_bigger = (measure(South) != None and measure(South) > measure())

				if left_bigger and (not down_bigger or measure(West) > measure(South)):
					swap(West)
					move(West)
				elif down_bigger:
					swap(South)
					move(South)
				else:
					break
	while not checkGroundAndHarvest(Entities.Cactus, False):
		pass

def plantCactusAll0(args):
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]
	isValidator = args["validator"]

	for y in range(endY, startY - 1, -1):
		for x in range(endX, startX -1, -1):
			goTo(x, y)
			checkGround(Grounds.Soil)
			if get_entity_type() != Entities.Cactus and not replant(Entities.Cactus):
				return
			size = measure()
			while size != 0:
				if not replant(Entities.Cactus):
					return
				size = measure()
		
	if not isValidator:
		return

	for x in range(startX, startX + 1):
		for y in range(startY, args["topY"] + 1):
			goTo(x, y)
			while not can_harvest() or measure() != 0:
				pass
	harvest()
			

def plantCactus(args):
	plantCactusAll0(args)

def main():
	N = get_world_size() - 1
	plantCactus({
		"startX": 0,
		"startY": 0,
		"endX": N,
		"endY": N
	})

if __name__ == "__main__":
	main()