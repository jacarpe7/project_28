# n refers to sensors 1 through 4
for n in range (5):
	r = open("dataBySensor/sensor" + str(n+1) + ".txt", "r")
	# one file each for train and test sets
	f1 = open("sensor" + str(n+1) + "-train.txt", "w")
	f2 = open("sensor" + str(n+1) + "-test.txt", "w")
	# v refers to the number of lines in each sensorN text file
	for v in range (1,301):
		# write to train set for 3 of every 4 lines
		if (v % 4 != 0):
			f1.write(r.readline())

		# write to test set for 1 of every 4 lines
		if (v % 4 == 0):
			f2.write(r.readline())

	r.close()
	f1.close()
	f2.close()
