#MainloopfileYO
import trafficlight as TL
import utility as UTIL

def createTrafficLights(n):
	lightList = []
	for i in range(n):
		lightList.append(TL.trafficLight(UTIL.test(),2,20,0.3,0.5))
		if (i>0):
			lightList[i].leftNeighbour = lightList[i-1]
			lightList[i-1].rightNeighbour = lightList[i]
	return lightList



Lights = createTrafficLights(3)
for l in lights:
	print l