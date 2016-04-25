class trafficLight:
	isGreen           = False
	CarCounterLeft    = 0
	carCounterRight   = 0
	spawnChanceLeft   = 0.0
	spawnChanceRight  = 0.0
	spawnPedestrianChance = 0.0
	overlapTime       = 0
	pedestrianCounter = 0
	minimumTimeSteps  = 0
	stepCounter       = 0
	leftNeighbour     = None
	rightNeighbour    = None
	utility_function  = None #Function?

	def __init__(self, utility_function, overlapTime, minimumTimeSteps, spawnChanceLeft, spawnChanceRight):
		self.utility_function = utility_function
		self.overlapTime = overlapTime
		self.minimumTimeSteps = minimumTimeSteps
		self.spawnChanceLeft = spawnChanceLeft
		self.spawnChanceRight = spawnChanceRight
