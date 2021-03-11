for n in range (1,10):
	r = open("sensor" + str(n) + ".txt", "r")
	f1 = open("sensor" + str(n) + "-train.txt", "w")
	f2 = open("sensor" + str(n) + "-test.txt", "w")
	for v in range (1,401):
		if (v % 4 != 0):
			f1.write(r.readline())

		if (v % 4 == 0):
			f2.write(r.readline())

	r.close()
	f1.close()
	f2.close()
