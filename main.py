#MainloopfileYO
import trafficlight as TL
import utility as UTIL

def createTrafficLights(n):
	lightList = []
	for i in range(n):
		#
		if i == 0:
			lightList.append(TL.trafficLight(UTIL.leftmost_utility,2,20,1.0,0.0))
		elif i == n-1:
			lightList.append(TL.trafficLight(UTIL.rightmost_utility,2,20,0.0,0.0))
		else:
			lightList.append(TL.trafficLight(UTIL.midle_utility,2,20,0.0,0.5))
		#
		if (i>0):
			lightList[i].leftNeighbour = lightList[i-1]
			lightList[i-1].rightNeighbour = lightList[i]
	return lightList



Lights = createTrafficLights(3)
for l in Lights:
	print (l.utility_function(l))