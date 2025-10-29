from moving_utils import *
from farm_utils import *

def pumpkinDrones(args):
	drones = []
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]
	
	for i in range(startX + 1, endX + 1):
		drones.append({
			"mainDrone": False,
			"args": {
				"validator": False,
				"startX": i,
				"startY": startY,
				"endX": i,
				"endY": endY
			}
		})
	drones.append({
		"mainDrone": True,
		"args": {
			"validator": True,
			"rightmostX": endX,
			"startX": startX,
			"startY": startY,
			"endX": startX,
			"endY": endY
		}
	})
	
	return drones	

def plantPumpkin(args):
	change_hat(Hats.Golden_Cactus_Hat)
	startX = args["startX"]
	startY = args["startY"]
	endX = args["endX"]
	endY = args["endY"]
	isValidator = args["validator"]
	
	goTo(startX, startY)

	dead = []

	for i in range(endX - startX + 1):
		for j in range(endY - startY + 1):
			dead.append(0)

	count = 0
	completed = False
	while not completed:
		checkGround(Grounds.Soil)
		if not replant(Entities.Pumpkin):
			return
		dead[-1 - count] = (get_pos_x(), get_pos_y())
		count += 1
		completed = traverseRect(startX, startY, endX, endY)
		
	while len(dead) > 0:
		for i in range(len(dead) - 1, -1, -1):
			goTo(dead[i][0], dead[i][1])
			if get_entity_type() == None:
				dead = []
				break
			if get_entity_type() == Entities.Dead_Pumpkin:
				if not replant(Entities.Pumpkin):
					return 
				useWaterIfBelowThreshold(0.75)
			else:
				if can_harvest():
					dead.pop(i)
				else:
					useWaterIfBelowThreshold(0.75)
	if isValidator:
		rightmostX = args["rightmostX"]
		bottomLeftId, upRightId = 0, 1
		while bottomLeftId != upRightId:
			goTo(startX, startY)
			bottomLeftId = measure()
			goTo(rightmostX, endY)
			upRightId = measure()
		harvest()
	
def main():
	N = get_world_size() - 1
	plantPumpkin({
		"startX": 0,
		"startY": 0,
		"endX": N,
		"endY": N
	})

if __name__ == "__main__":
	main()