class trafficLight:
	isGreen           = False
	CarCounterLeft    = 0
	carCounterRight   = 0
	spawnChanceLeft   = 0.0
	spawnChanceRight  = 0.0
	overlapTime       = 0
	pedestrianCounter = 0
	minimumTimeSteps  = 0
	stepCounter       = 0
	utility_function  = None #Function?
	leftNeighbour     = None
	rightNeighbour    = None

	def __init__(self, utility_function, overlapTime, minimumTimeSteps, spawnChanceLeft, spawnChanceRight):
		self.utility_function = utility_function
		self.overlapTime = overlapTime
		self.minimumTimeSteps = minimumTimeSteps
		self.spawnChanceLeft = spawnChanceLeft
		self.spawnChanceRight = spawnChanceRight

	def evaluateChange(self):
		pass

	def move(self):
		if self.isGreen:
			if CarCounterLeft >= 1:
				CarCounterLeft -= 1
				if rightNeighbour:
					rightNeighbour.CarCounterLeft += 1
			if carCounterRight >= 1:
				carCounterRight -= 1
				if leftNeighbour:
					leftNeighbour.carCounterRight += 1
		else:
			pedestrianCounter = 0


