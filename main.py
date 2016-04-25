#MainloopfileYOLOSWAG
import trafficlight as TL
import utility as UTIL

# -- Default values --
overlapTime      = 2
minimumTimeSteps = 20
spawnChanceLeft  = 0.5
spawnChanceRight = 0.5
# -- Default values --

def createTrafficLights(n):
	lightList = []
	for i in range(n):
		if i == 0:
			lightList.append(TL.trafficLight(UTIL.leftmost_utility,overlapTime,minimumTimeSteps,spawnChanceLeft,spawnChanceRight))
		if i == n-1:
			lightList.append(TL.trafficLight(UTIL.rightmost_utility,overlapTime,minimumTimeSteps,spawnChanceLeft,spawnChanceRight))
		else:
			lightList.append(TL.trafficLight(UTIL.midle_utility,overlapTime,minimumTimeSteps,spawnChanceLeft,spawnChanceRight))
		if (i>0): # If this is not the only light, set neighbours.
			lightList[i].leftNeighbour      = lightList[i-1]
			lightList[i].spawnChanceLeft    = 0
			lightList[i-1].rightNeighbour   = lightList[i]
			lightList[i-1].spawnChanceRight = 0
	return lightList

lights = createTrafficLights(3)
lightsToEvaluate = []


timestep = 0
while timestep < 100:
	for light in lights:
		if (light.stepCounter >= light.minimumTimeSteps):
			lightsToEvaluate.append(light) #Light has run for minimum time, and should evaluate a light change
		else:
			light.move() # Light moves cars or pedestrians
	for light in lights:
		light.spawnEntities() # Spawns cars and pedestrians
	if lightsToEvaluate:
		for light in lightsToEvaluate:
			light.evaluateChange() # Gives each light hat has run the given timesteps to evaluate if it should have green or red light
		lightsToEvaluate = []
	timestep += 1
