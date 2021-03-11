filelist = list()
filelist += ['selection','swipe_left','swipe_right','swipe_up']

for n in range (1,10):
	f = open("sensor" + str(n) + ".txt", "w")
	for file in filelist:
		if (n == 9):
			n = 0
		r = open('output-'+file+'.txt', "r")
		for i in range(1,901):
			text = r.readline()
			if (i % 9 == n):
				f.write(text)

		r.close()

	f.close()

