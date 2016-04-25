class trafficLight:
	isGreen = False
	CarCounterA = 0
	carCounterB = 0
	SpawnChanceA = 0.0
	SpawnChanceB = 0.0
	overlapTime = 2
	pedestrianCounter = int
	minimumTimeSteps = int
	greenCounter = int #How many timesteps has passed while light has been green.
	leftNeighbour = traffic_light object
	rightNeighbours = traffic_light object
	utility_function = function()