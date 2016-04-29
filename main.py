#Mainloopfile
import trafficlight as TL
import utility as UTIL
import time
# -- Default values --
overlapTime           = 2
minimumTimeStepsCar   = 30
minimumTimeStepsPed   = 20
spawnChanceLeft       = 0.55
spawnChanceRight      = 0.55
averageChanceCar      = (spawnChanceRight+spawnChanceLeft)/2
spawnPedestrianChance = 0.4
# -- Default values --

def createTrafficLights(n):
	lightList = []
	for i in range(n):
		if i == 0:
			lightList.append(TL.trafficLight(UTIL.leftmost_utility,overlapTime,minimumTimeStepsCar, minimumTimeStepsPed,spawnChanceLeft,spawnChanceRight,spawnPedestrianChance))
		elif i == n-1:
			lightList.append(TL.trafficLight(UTIL.rightmost_utility,overlapTime,minimumTimeStepsCar, minimumTimeStepsPed,spawnChanceLeft,spawnChanceRight,spawnPedestrianChance))
		else:
			lightList.append(TL.trafficLight(UTIL.midle_utility,overlapTime,minimumTimeStepsCar, minimumTimeStepsPed,spawnChanceLeft,spawnChanceRight,spawnPedestrianChance))
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

lights = createTrafficLights(10) # This line generates the traffic lights. The input is the number of lights to be created
lightsToEvaluate = [] # Used at the end of a timestep to see which lights needs to evaluate green/red

totalThroughCars = 0 	# Statistic purposes
totalThroughPed = 0  	# Statistic purposes
timeOfArrivalRight = [] # Statistic purposes
timeofArrivalLeft = []  # Statistic purposes
timeOfDepartureRight = [] # Statistic purposes
timeOfDepartureLeft = []  # Statistic purposes
avg_ped_wait = []   	# Statistic purposes

timestep = 0
while timestep < 100000: # This is the main loop. Each light may move one car in each direction per timestep if the light is green, or move all pedestrians if the light is red
	print ("timestep #",timestep)
	time.sleep(0.5)      # This is only to slow the visualization down
	print_visualisation(lights) #Prints a visualization of the simulated lights.

	for light in lights:
		l, r = light.spawnEntities(timestep) # Spawns cars and pedestrians
		if l != 0:
			timeofArrivalLeft.append(l)	# A car was spawned on the left side (light[0])
		if r != 0:
			timeOfArrivalRight.append(r) # A car was spawned on the right side (light[-1])
	for light in lights:
		if (light.isGreen) and (light.stepCounter >= light.minimumTimeStepsCar): #Light has run for minimum time, and should evaluate a light change
			lightsToEvaluate.append(light)
		elif (not light.isGreen) and (light.stepCounter >= light.minimumTimeStepsPed): #Light has run for minimum time, and should evaluate a light change
			lightsToEvaluate.append(light)
		else:
			c, lDep, rDep, pedArr, pedmoved = light.move(timestep) # Light moves cars or pedestrians
			#Lines below are for statistics only
			totalThroughCars += c
			totalThroughPed  += pedmoved
			if lDep != 0:
				timeOfDepartureLeft.append(lDep)
			if rDep != 0:
				timeOfDepartureRight.append(rDep)
			if pedArr:
				avg_ped_wait.append(pedArr)

	if lightsToEvaluate:
		for light in lightsToEvaluate:
			light.evaluateChange(averageChanceCar,spawnPedestrianChance) # Gives each light that has run the given timesteps to evaluate if it should turn green or red light
		lightsToEvaluate = []
	timestep += 1


# The rest of the code is only for statistic purposes
print_visualisation(lights)
print ("TotalThroughPutCars: ", totalThroughCars)
print ("TotalThroughPutPedestrians: ", totalThroughPed)

avg_wait_right = 0
for i in range (len(timeOfDepartureRight)):
	avg_wait_right += timeOfDepartureRight[i] - timeOfArrivalRight[i]
avg_wait_right = avg_wait_right/(len(timeOfDepartureRight))


avg_wait_left = 0
for i in range (len(timeOfDepartureLeft)):
	avg_wait_left += timeOfDepartureLeft[i] - timeofArrivalLeft[i]
avg_wait_left = avg_wait_left/(len(timeOfDepartureLeft))
avg_wait_cars = (avg_wait_left+avg_wait_right)/2
print ("avg_wait_cars", avg_wait_cars)

if spawnPedestrianChance != 0:
	temp_ped_wait = 0
	for i in avg_ped_wait:
		temp_ped_wait += i
	avg_ped_wait = temp_ped_wait / (len(avg_ped_wait))
	print ("avg_ped_wait", avg_ped_wait)

print ("total wait time cars: ", avg_wait_cars*totalThroughCars)
if spawnPedestrianChance != 0:
	print ("total wait time peds: ", avg_ped_wait*totalThroughPed)
if spawnPedestrianChance != 0:
	print ("Total wait time: ", ((avg_ped_wait*totalThroughPed)+avg_wait_cars*totalThroughCars)/1000 )
else:
	print ("Total wait time: ", (avg_wait_cars*totalThroughCars)/1000 )


