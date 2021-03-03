for n in range (1,5):
	r = open("sensor" + str(n) + ".txt", "r")
	f1 = open("sensor" + str(n) + "-train.txt", "w")
	f2 = open("sensor" + str(n) + "-test.txt", "w")
	for v in range (1,5):
		for i in range (1,151):
			f1.write(r.readline())

		for i in range (151,201):
			f2.write(r.readline())
