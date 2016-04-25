#MainloopfileYOLOSWAG
import trafficlight as TL
import utility as UTIL
import time
# -- Default values --
overlapTime           = 2
minimumTimeSteps      = 20
spawnChanceLeft       = 0.2
spawnChanceRight      = 0.6
spawnPedestrianChance = 0.5
# -- Default values --

def createTrafficLights(n):
	lightList = []
	for i in range(n):
		if i == 0:
			lightList.append(TL.trafficLight(UTIL.leftmost_utility,overlapTime,minimumTimeSteps,spawnChanceLeft,spawnChanceRight,spawnPedestrianChance))
		elif i == n-1:
			lightList.append(TL.trafficLight(UTIL.rightmost_utility,overlapTime,minimumTimeSteps,spawnChanceLeft,spawnChanceRight,spawnPedestrianChance))
		else:
			lightList.append(TL.trafficLight(UTIL.midle_utility,overlapTime,minimumTimeSteps,spawnChanceLeft,spawnChanceRight,spawnPedestrianChance))
		if (i>0): # If this is not the only light, set neighbours.
			lightList[i].leftNeighbour      = lightList[i-1]
			lightList[i].spawnChanceLeft    = 0
			lightList[i-1].rightNeighbour   = lightList[i]
			lightList[i-1].spawnChanceRight = 0
	return lightList

def print_visualisation(lights):
	s = ""
	for l in lights:
		s += '{:<6}'.format(str(l.isGreen))
	print (s+" | Green light")
	s = ""
	for l in lights:
		s += '{:<6}'.format(str(l.carCounterRight))
	print (s+" | carCounterRight")
	s = ""
	for l in lights:
		s += '{:<6}'.format(str(l.carCounterLeft))
	print (s+" | carCounterLeft")
	s = ""
	for l in lights:
		s += '{:<6}'.format(str(l.pedestrianCounter))
	print (s+" | pedestrianCounter")
	print("")

lights = createTrafficLights(5)
lightsToEvaluate = []

timestep = 0
while timestep < 10000:
	time.sleep(0.1)
	print_visualisation(lights)
	for light in lights:
		light.spawnEntities() # Spawns cars and pedestrians

	for light in lights:
		if (light.stepCounter >= light.minimumTimeSteps):
			lightsToEvaluate.append(light) #Light has run for minimum time, and should evaluate a light change
		else:
			light.move() # Light moves cars or pedestrians

	if lightsToEvaluate:
		for light in lightsToEvaluate:
			light.evaluateChange() # Gives each light hat has run the given timesteps to evaluate if it should have green or red light
		lightsToEvaluate = []
	timestep += 1
