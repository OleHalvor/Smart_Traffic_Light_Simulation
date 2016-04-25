import random as rng

class trafficLight:
	isGreen               = False
	CarCounterLeft        = 0
	carCounterRight       = 0
	spawnChanceLeft       = 0.0
	spawnChanceRight      = 0.0
	overlapTime           = 0
	pedestrianCounter     = 0
	spawnPedestrianChance = 0
	minimumTimeSteps      = 0
	stepCounter           = 0
	utility_function      = None #Function?
	leftNeighbour         = None
	rightNeighbour        = None

	def __init__(self, utility_function, overlapTime, minimumTimeSteps, spawnChanceLeft, spawnChanceRight):
		self.utility_function = utility_function
		self.overlapTime      = overlapTime
		self.minimumTimeSteps = minimumTimeSteps
		self.spawnChanceLeft  = spawnChanceLeft
		self.spawnChanceRight = spawnChanceRight

	def evaluateChange(self):
		if self.isGreen:
			isGreen = False
		else:
			isGreen = True

	def spawnEntities(self):
		if spawnChanceLeft > 0:
			if (rng.random() < spawnChanceLeft):
				self.CarCounterLeft    += 1
		if spawnChanceRight > 0:
			if (rng.random() < spawnChanceRight):
				self.carCounterRight   += 1
		if spawnPedestrianChance > 0:
			if (rng.random() < spawnPedestrianChance):
				self.pedestrianCounter += 1



	def move(self):
		if self.isGreen:
			if CarCounterLeft  >= 1:
				CarCounterLeft -= 1
				if rightNeighbour:
					rightNeighbour.CarCounterLeft += 1
			if carCounterRight  >= 1:
				carCounterRight -= 1
				if leftNeighbour:
					leftNeighbour.carCounterRight += 1
		else:
			pedestrianCounter = 0


