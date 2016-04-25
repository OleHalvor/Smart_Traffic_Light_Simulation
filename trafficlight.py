class trafficLight:
	isGreen           = False
	CarCounterLeft    = 0
	carCounterRight   = 0
	SpawnChanceLeft   = 0.0
	SpawnChanceRight  = 0.0
	overlapTime       = 0
	pedestrianCounter = 0
	minimumTimeSteps  = 0
	stepCounter       = 0
	leftNeighbour     = None
	rightNeighbours   = None
	utility_function  = None #Function?