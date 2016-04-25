def midle_utility(l):
	print("utility middle")
	utility = []
	if l.rightNeighbour.isGreen:
		if l.leftNeighbour.isGreen:
			#Få grønt, gitt de har grønt
			carsLeft = max(l.CarCounterLeft + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight) - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.leftNeighbour.CarCounterLeft) - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))
			
			#Få rødt lys
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.leftNeighbour.CarCounterLeft), 0)
			carsLeft = max(l.CarCounterLeft + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight), 0)
			utility.append(carsLeft + carsRight)
		else:
			#Få grønt, left er rodt
			carsLeft = max(l.CarCounterLeft - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.leftNeighbour.CarCounterLeft) - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))

			#Få roedt
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.leftNeighbour.CarCounterLeft), 0)
			carsLeft = max(l.CarCounterLeft, 0)
			utility.append(carsLeft + carsRight)
	else:
		if l.leftNeighbour.isGreen:
			#Få grønt
			carsLeft = max(l.CarCounterLeft + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight) - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))
			
			#Få rødt lys
			carsLeft = max(l.CarCounterLeft + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight), 0)
			carsRight = max(l.carCounterRight, 0)
			utility.append(carsLeft + carsRight)
		else:
			#Få grønt
			carsLeft = max(l.CarCounterLeft - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))

			#Få roedt
			carsRight = max(l.carCounterRight, 0)
			carsLeft = max(l.CarCounterLeft, 0)
			utility.append(carsLeft + carsRight)
	#
	return utility.index(min(utility))
#
def leftmost_utility(l):
	print("utility left")
	utility = []

	if l.rightNeighbour.isGreen:

		#Få grønt, gitt han har grønt
		carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.leftNeighbour.CarCounterLeft) - l.minimumTimeSteps, 0)
		carsLeft  = max(l.CarCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft - l.minimumTimeSteps, 0)
		utility.append(carsRight + carsLeft + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))
	
		#Få rødt lys
		carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.leftNeighbour.CarCounterLeft), 0)
		carsLeft  = max(l.CarCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft, 0)
		utility.append(carsLeft + carsRight)
	else:
		#Få grønt, gitt han har rødt
		carsRight = max(l.carCounterRight - l.minimumTimeSteps, 0)
		carsLeft  = max(l.CarCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft - l.minimumTimeSteps, 0)
		utility.append(carsRight + carsLeft + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))
	
		#Få rødt lys
		carsRight = max(l.carCounterRight, 0)
		carsLeft  = max(l.CarCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft, 0)
		utility.append(carsLeft + carsRight)
	#
	return utility.index(min(utility))
#
def rightmost_utility(l):
	print("utility right")
	utility = []

	if l.leftNeighbour.isGreen:

		#Få Grønt
		carsLeft = max(l.CarCounterLeft + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight) - l.minimumTimeSteps, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight - l.minimumTimeSteps, 0)

		utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))
		
		#Få rødt lys
		carsLeft = max(l.CarCounterLeft + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight), 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight, 0)
		utility.append(carsLeft + carsRight)
	else:
		#Få Grønt
		carsLeft = max(l.CarCounterLeft - l.minimumTimeSteps, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight - l.minimumTimeSteps, 0)

		utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/3))
		
		#Få rødt lys
		carsLeft = max(l.CarCounterLeft, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight, 0)
		utility.append(carsLeft + carsRight)
	#
	return utility.index(min(utility))