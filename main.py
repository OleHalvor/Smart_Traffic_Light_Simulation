#MainloopfileYOLOSWAG
import trafficlight as TL
import utility as UTIL

# -- Default values --
overlapTime      = 2
minimumTimeSteps = 20
spawnChanceLeft  = 0.3
spawnChanceRight = 0.5
# -- Default values --

def createTrafficLights(n):
	lightList = []
	for i in range(n):
		lightList.append(TL.trafficLight(UTIL.test(),overlapTime,minimumTimeSteps,spawnChanceLeft,spawnChanceRight))
		if (i>0):
			lightList[i].leftNeighbour      = lightList[i-1]
			lightList[i].spawnChanceLeft    = 0
			lightList[i-1].rightNeighbour   = lightList[i]
			lightList[i-1].spawnChanceRight = 0
	return lightList

lights = createTrafficLights(3)
lightsToEvaluate = []

while timestep < 100:
	for light in lights:
		if (light.stepCounter >= light.minimumTimeSteps):
			lightsToEvaluate.append(light)
		else:
			light.move()
	if lightsToEvaluate:
		for light in lightsToEvaluate:
			light.evaluateChange
	timestep += 1