from itemsSource import itemsSource
from plantsLogic import plantsLogic

def farm(plantType, totalAmount):
	clear()

	if plantType != "weirdSubstance":
		cost = get_cost(plantType)
	else:
		cost = {}
	currPlant = plantsLogic[plantType]
	squareSize = ((currPlant["args"]["endX"] - currPlant["args"]["startX"] + 1) *
		(currPlant["args"]["endY"] - currPlant["args"]["startY"] + 1)
	)

	while num_items(currPlant["item"]) < totalAmount:
		for item in cost:
			if num_items(item) < cost[item] * squareSize * currPlant["costOverhead"]:
				farm(itemsSource[item], cost[item] * squareSize * currPlant["costOverhead"])
	
		if plantType != Entities.Sunflower and num_items(Items.Power) < currPlant["minEnergy"]:
			farm(Entities.Sunflower, currPlant["maxEnergy"])

		while num_drones() != 1:
			pass

		for drone in currPlant["multiDronesfunc"](currPlant["args"]):
			def split():
				currPlant["func"](drone["args"])
			if not drone["mainDrone"]:
				spawn_drone(split)
			else:
				split()
			
def main():
	unlocks = [
		(Unlocks.Top_Hat, 0)
	]
	
	for (unlock_, level) in unlocks:
		while num_unlocked(unlock_) <= level:
			costs = get_cost(unlock_, level)
			for item in costs:
				farm(itemsSource[item], costs[item])
			unlock(unlock_)

	# infinite farm when idle
	resources = [
		(Entities.Dinosaur, 1),
		(Entities.Cactus, 1),
		(Entities.Treasure, 1),
		(Entities.Pumpkin, 10),
		(Entities.Carrot, 10),
		("weirdSubstance", 100),
		(Entities.Tree, 100),
		(Entities.Grass, 100)
	]
	
	while True:
		for (res, mult) in resources:
			farm(res, num_items(plantsLogic[res]["item"]) + 1000000 * mult)

if __name__ == "__main__":
	main()