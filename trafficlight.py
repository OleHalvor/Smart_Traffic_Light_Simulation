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
	pedestrianArrivals    = []

	def __init__(self, utility_function, overlapTime, minimumTimeSteps, spawnChanceLeft, spawnChanceRight, spawnPedestrianChance):
		self.utility_function      = utility_function
		self.overlapTime           = overlapTime
		self.minimumTimeSteps      = minimumTimeSteps# + (rng.random()*4)
		self.spawnChanceLeft       = spawnChanceLeft
		self.spawnChanceRight      = spawnChanceRight
		self.spawnPedestrianChance = spawnPedestrianChance

	def evaluateChange(self,averageChanceCar,spawnPedestrianChance): # Use utility function here
		flipswitch = True
		if not flipswitch:
			if self.utility_function(self,averageChanceCar,spawnPedestrianChance) == 0:
				self.isGreen = True
			else:
				self.isGreen = False
		else:
			if self.isGreen:
				self.isGreen = False
			else:
				self.isGreen = True
		self.stepCounter = 0

	def spawnEntities(self, timestep):
		leftSpawn = 0
		rightSpawn = 0
		if self.spawnChanceLeft > 0:
			if (rng.random() < self.spawnChanceLeft):
				self.carCounterLeft    += 1
				leftSpawn = timestep
		if self.spawnChanceRight > 0:
			if (rng.random() < self.spawnChanceRight):
				self.carCounterRight   += 1
				rightSpawn = timestep
		if self.spawnPedestrianChance > 0:
			if (rng.random() < self.spawnPedestrianChance):
				self.pedestrianCounter += 1
				self.pedestrianArrivals.append(timestep)

		return leftSpawn, rightSpawn



	def move(self, timestep):
		c = 0
		rDep = 0
		lDep = 0
		pedArr = []
		pedmoved = 0
		if self.isGreen:
			if self.carCounterLeft  >= 1:
				self.carCounterLeft -= 1
				if self.rightNeighbour:
					self.rightNeighbour.carCounterLeft += 1
				else:
					c += 1
					lDep = timestep
			if self.carCounterRight  >= 1:
				self.carCounterRight -= 1

				if self.leftNeighbour:
					self.leftNeighbour.carCounterRight += 1
				else:
					c += 1
					rDep = timestep

		else:
			pedmoved = self.pedestrianCounter
			self.pedestrianCounter = 0
			if self.pedestrianArrivals:
				temp = 0
				for i in range (len(self.pedestrianArrivals)):
					temp += timestep - self.pedestrianArrivals[i]
				pedArr = temp / (len(self.pedestrianArrivals))
				self.pedestrianArrivals = []



		self.stepCounter += 1
		return c, lDep, rDep, pedArr, pedmoved




