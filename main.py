#MainloopfileYO
import trafficlight as TL
import utility as UTIL

# -- Default values --
overlapTime = 2
minimumTimeSteps = 20
spawnChanceLeft = 0.3
spawnChanceRight = 0.5

def createTrafficLights(n):
	lightList = []
	for i in range(n):
		lightList.append(TL.trafficLight(UTIL.test(),2,20,0.3,0.5))
		if (i>0):
			lightList[i].leftNeighbour = lightList[i-1]
			lightList[i].spawnChanceLeft = 0
			lightList[i-1].rightNeighbour = lightList[i]
			lightList[i-1].spawnChanceRight = 0
	return lightList
