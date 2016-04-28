
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
			carsLeft = max(l.carCounterLeft + min(l.getRemainingSteps(), l.leftNeighbour.carCounterLeft) - l.minimumTimeStepsCar, 0)
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.getRemainingSteps(), l.rightNeighbour.carCounterRight) - l.minimumTimeStepsCar, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeStepsCar*l.spawnPedestrianChance)/cars_to_peds_weight))

			#Få rødt lys
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.getRemainingSteps(), l.rightNeighbour.carCounterRight), 0)
			carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.getRemainingSteps(), l.leftNeighbour.carCounterLeft), 0)
			utility.append(carsLeft + carsRight)
		else:
			#Få grønt, left er rodt
			carsLeft = max(l.carCounterLeft - l.minimumTimeStepsCar, 0)
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.getRemainingSteps(), l.rightNeighbour.carCounterRight) - l.minimumTimeStepsCar, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.getRemainingSteps()*l.spawnPedestrianChance)/cars_to_peds_weight))

			#Få roedt
			carsRight = max(l.carCounterRight + min(l.rightNeighbour.getRemainingSteps(), l.rightNeighbour.carCounterRight), 0)
			carsLeft = max(l.carCounterLeft, 0)
			utility.append(carsLeft + carsRight)
	else:
		if l.leftNeighbour.isGreen:
			#Få grønt
			carsLeft = max(l.carCounterLeft + min(l.rightNeighbour.getRemainingSteps(), l.leftNeighbour.carCounterLeft) - l.minimumTimeStepsCar, 0)
			carsRight = max(l.carCounterRight - l.minimumTimeStepsCar, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeStepsCar*l.spawnPedestrianChance)/cars_to_peds_weight))

			#Få rødt lys
			carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.getRemainingSteps(), l.leftNeighbour.carCounterLeft), 0)
			carsRight = max(l.carCounterRight, 0)
			utility.append(carsLeft + carsRight)
		else:
			#Få grønt
			carsLeft = max(l.carCounterLeft - l.minimumTimeStepsCar, 0)
			carsRight = max(l.carCounterRight - l.minimumTimeStepsCar, 0)

			utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeStepsCar*l.spawnPedestrianChance)/cars_to_peds_weight))

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
		carsRight = max(l.carCounterRight + min(l.rightNeighbour.getRemainingSteps(), l.rightNeighbour.carCounterRight) - l.minimumTimeStepsCar, 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeStepsCar*l.spawnChanceLeft - l.minimumTimeStepsCar, 0)
		utility.append(carsRight + carsLeft + ((l.pedestrianCounter + l.minimumTimeStepsCar*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsRight = max(l.carCounterRight + min(l.rightNeighbour.getRemainingSteps(), l.rightNeighbour.carCounterRight), 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeStepsCar*l.spawnChanceLeft, 0)
		utility.append(carsLeft + carsRight)
	else:
		#Få grønt, gitt han har rødt
		carsRight = max(l.carCounterRight - l.minimumTimeStepsCar, 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeStepsCar*l.spawnChanceLeft - l.minimumTimeStepsCar, 0)
		utility.append(carsRight + carsLeft + ((l.pedestrianCounter + l.minimumTimeStepsCar*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsRight = max(l.carCounterRight, 0)
		carsLeft  = max(l.carCounterLeft + l.minimumTimeStepsCar*l.spawnChanceLeft, 0)
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
		carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.getRemainingSteps(), l.leftNeighbour.carCounterLeft) - l.minimumTimeStepsCar, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeStepsCar*l.spawnChanceRight - l.minimumTimeStepsCar, 0)

		utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeStepsCar*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsLeft = max(l.carCounterLeft + min(l.leftNeighbour.getRemainingSteps(), l.leftNeighbour.carCounterLeft), 0)
		carsRight = max(l.carCounterRight + l.minimumTimeStepsCar*l.spawnChanceRight, 0)
		utility.append(carsLeft + carsRight)
	else:
		#Få Grønt
		carsLeft = max(l.carCounterLeft - l.minimumTimeStepsCar, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeStepsCar*l.spawnChanceRight - l.minimumTimeStepsCar, 0)

		utility.append(carsLeft + carsRight + ((l.pedestrianCounter + l.minimumTimeStepsCar*l.spawnPedestrianChance)/cars_to_peds_weight))

		#Få rødt lys
		carsLeft = max(l.carCounterLeft, 0)
		carsRight = max(l.carCounterRight + l.minimumTimeStepsCar*l.spawnChanceRight, 0)
		utility.append(carsLeft + carsRight)
	#
	return utility.index(min(utility))