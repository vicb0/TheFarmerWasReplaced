from pumpkin import *
from grass import *
from carrot import *
from tree import *
from carrot import *
from sunflower import *
from cactus import *
from bone import *
from weirdSubstance import *
from treasure import *

N = get_world_size() - 1

plantsLogic = {
	Entities.Grass: {
		"item": Items.Hay,
		"func": plantGrass,
		"multiDronesfunc": grassDrones,
		"minEnergy": 100,
		"maxEnergy": 500,
		"args": {
			"startX": 3,
			"startY": 3,
			"endX": 10,
			"endY": 10
		}
	},
	Entities.Tree: {
		"item": Items.Wood,
		"func": plantTree,
		"multiDronesfunc": woodDrones,
		"minEnergy": 200,
		"maxEnergy": 1000,
		"args": {
			"startX": 3,
			"startY": 3,
			"endX": 10,
			"endY": 10
		}
	},
	Entities.Carrot: {
		"item": Items.Carrot,
		"func": plantCarrot,
		"multiDronesfunc": carrotDrones,
		"minEnergy": 200,
		"maxEnergy": 1000,
		"costOverhead": 4,
		"args": {
			"startX": 3,
			"startY": 3,
			"endX": 10,
			"endY": 10
		}
	},
	Entities.Pumpkin: {
		"item": Items.Pumpkin,
		"func": plantPumpkin,
		"multiDronesfunc": pumpkinDrones,
		"minEnergy": 300,
		"maxEnergy": 1500,
		"costOverhead": 2,
		"args": {
			"startX": 0,
			"startY": 0,
			"endX": N,
			"endY": N
		}
	},
	Entities.Sunflower: {
		"item": Items.Power,
		"func": plantSunflower,
		"multiDronesfunc": sunflowerDrones,
		"costOverhead": 10,
		"args": {
			"startX": 0,
			"startY": 0,
			"endX": N,
			"endY": N
		}
	},
	Entities.Cactus: {
		"item": Items.Cactus,
		"func": plantCactus,
		"costOverhead": 20,
		"multiDronesfunc": cactusDrones,
		"minEnergy": 1000,
		"maxEnergy": 1000,
		"args": {
			"startX": 0,
			"startY": 0,
			"endX": N,
			"endY": N
		}
	},
	Entities.Dinosaur: {
		"item": Items.Bone,
		"func": snakeGame,
		"multiDronesfunc": boneDrones,
		"costOverhead": 1,
		"minEnergy": 2000,
		"maxEnergy": 2000,
		"args": {
			"startX": 0,
			"startY": 0,
			"endX": N,
			"endY": N,
			"timeLimit": 7.5
		}
	},
	"weirdSubstance": {
		"item": Items.Weird_Substance,
		"multiDronesfunc": weirdSubstanceDrones,
		"func": farmWeirdSubstance,
		"minEnergy": 100,
		"maxEnergy": 500,
		"args": {
			"startX": 3,
			"startY": 3,
			"endX": 3,
			"endY": 3
		}
	},
	Entities.Treasure: {
		"item": Items.Gold,
		"func": solveMaze,
		"multiDronesfunc": treasureDrones,
		"costOverhead": 32,
		"minEnergy": 1000,
		"maxEnergy": 1000,
		"args": {
			"startX": 0,
			"startY": 0,
			"endX": 0,
			"endY": 0
		}
	}
}