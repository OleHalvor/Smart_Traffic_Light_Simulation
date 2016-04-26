import random as rng

class trafficLight:
	isGreen               = False
	carCounterLeft        = 0
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

	def __init__(self, utility_function, overlapTime, minimumTimeSteps, spawnChanceLeft, spawnChanceRight, spawnPedestrianChance):
		self.utility_function      = utility_function
		self.overlapTime           = overlapTime
		self.minimumTimeSteps      = minimumTimeSteps
		self.spawnChanceLeft       = spawnChanceLeft
		self.spawnChanceRight      = spawnChanceRight
		self.spawnPedestrianChance = spawnPedestrianChance

	def evaluateChange(self): # Use utility function here
		if self.utility_function(self) == 0:
			self.isGreen = True
		else:
			self.isGreen = False
		# if self.isGreen:
		# 	self.isGreen = False
		# else:
		# 	self.isGreen = True
		self.stepCounter = 0

	def spawnEntities(self):
		if self.spawnChanceLeft > 0:
			if (rng.random() < self.spawnChanceLeft):
				self.carCounterLeft    += 1
		if self.spawnChanceRight > 0:
			if (rng.random() < self.spawnChanceRight):
				self.carCounterRight   += 1
		if self.spawnPedestrianChance > 0:
			if (rng.random() < self.spawnPedestrianChance):
				self.pedestrianCounter += 1

	def move(self):

		if self.isGreen:
			if self.carCounterLeft  >= 1:
				self.carCounterLeft -= 1
				if self.rightNeighbour:
					self.rightNeighbour.carCounterLeft += 1
			if self.carCounterRight  >= 1:
				self.carCounterRight -= 1
				if self.leftNeighbour:
					self.leftNeighbour.carCounterRight += 1
		else:
			self.pedestrianCounter = 0
		self.stepCounter += 1


