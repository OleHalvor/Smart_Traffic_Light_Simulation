
def midle_utility(l,averageChanceCar,spawnPedestrianChance):
	if spawnPedestrianChance == 0:
		cars_to_peds_weight = 3
	else:
		cars_to_peds_weight = 3 * (averageChanceCar/spawnPedestrianChance)

	# print("utility middle")
	utility = []
	if l.rightNeighbour.isGreen:
		if l.leftNeighbour.isGreen:
			#Få grønt, gitt de har grønt
			carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.minimumTimeSteps-l.leftNeighbour.stepCounter, l.leftNeighbour.carCounterLeft) - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight) - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

			#Få rødt lys
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight), 0)
			carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.minimumTimeSteps-l.leftNeighbour.stepCounter, l.leftNeighbour.carCounterLeft), 0)
			utility.append(carsLeft + carsRight)
		else:
			#Få grønt, left er rodt
			carsLeft = max(l.carCounterLeft - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight) - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

			#Få roedt
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight), 0)
			carsLeft = max(l.carCounterLeft, 0)
			utility.append(carsLeft + carsRight)
	else:
		if l.leftNeighbour.isGreen:
			#Få grønt
			carsLeft = max(l.carCounterLeft + min(l.rightNeighbour.minimumTimeSteps-l.leftNeighbour.stepCounter, l.leftNeighbour.carCounterLeft) - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

			#Få rødt lys
			carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.minimumTimeSteps-l.leftNeighbour.stepCounter, l.leftNeighbour.carCounterLeft), 0)
			carsRight = max(l.carCounterRight, 0)
			utility.append(carsLeft + carsRight)
		else:
			#Få grønt
			carsLeft = max(l.carCounterLeft - l.minimumTimeSteps, 0)
			carsRight = max(l.carCounterRight - l.minimumTimeSteps, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

			#Få roedt
			carsRight = max(l.carCounterRight, 0)
			carsLeft = max(l.carCounterLeft, 0)
			utility.append(carsLeft + carsRight)
	#
	return utility.index(min(utility))
#
def leftmost_utility(l,averageChanceCar,spawnPedestrianChance):
	# print("utility left")
	if spawnPedestrianChance == 0:
		cars_to_peds_weight = 3
	else:
		cars_to_peds_weight = 3 * (averageChanceCar/spawnPedestrianChance)
	utility = []

	if l.rightNeighbour.isGreen:

		#Få grønt, gitt han har grønt
		carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight) - l.minimumTimeSteps, 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft - l.minimumTimeSteps, 0)
		utility.append(carsRight + carsLeft + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsRight = max(l.carCounterRight + min(l.rightNeighbour.minimumTimeSteps-l.rightNeighbour.stepCounter, l.rightNeighbour.carCounterRight), 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft, 0)
		utility.append(carsLeft + carsRight)
	else:
		#Få grønt, gitt han har rødt
		carsRight = max(l.carCounterRight - l.minimumTimeSteps, 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft - l.minimumTimeSteps, 0)
		utility.append(carsRight + carsLeft + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsRight = max(l.carCounterRight, 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeSteps*l.spawnChanceLeft, 0)
		utility.append(carsLeft + carsRight)
	#
	return utility.index(min(utility))
#
def rightmost_utility(l,averageChanceCar,spawnPedestrianChance):
	if spawnPedestrianChance == 0:
		cars_to_peds_weight = 3
	else:
		cars_to_peds_weight = 3 * (averageChanceCar/spawnPedestrianChance)
	# print("utility right")
	utility = []

	if l.leftNeighbour.isGreen:

		#Få Grønt
		carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.minimumTimeSteps-l.leftNeighbour.stepCounter, l.leftNeighbour.carCounterLeft) - l.minimumTimeSteps, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight - l.minimumTimeSteps, 0)

		utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.minimumTimeSteps-l.leftNeighbour.stepCounter, l.leftNeighbour.carCounterLeft), 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight, 0)
		utility.append(carsLeft + carsRight)
	else:
		#Få Grønt
		carsLeft = max(l.carCounterLeft - l.minimumTimeSteps, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight - l.minimumTimeSteps, 0)

		utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeSteps*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsLeft = max(l.carCounterLeft, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeSteps*l.spawnChanceRight, 0)
		utility.append(carsLeft + carsRight)
	#
	return utility.index(min(utility))