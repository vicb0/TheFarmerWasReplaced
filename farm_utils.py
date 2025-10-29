from plantsGround import plantsGround

def replant(plantType):
	harvest()
	return plant(plantType)

def checkGround(desiredGround):	
	if get_ground_type() != desiredGround:
		till()

def checkGroundAndHarvest(plantType, doReplant=True):
	checkGround(plantsGround[plantType])

	if get_entity_type() == plantType and not can_harvest():
		useWaterIfBelowThreshold(0.75)
	else:
		if doReplant:
			if not replant(plantType):
				return -1
			return True
		return harvest()
	return False

def useWaterIfBelowThreshold(threshold):
	if get_water() < threshold:
		use_item(Items.Water)
		
def getCompanion():
	companion = get_companion()
	if companion != None:
		return companion
	return (None, (None, None))
		