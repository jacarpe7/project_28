filelist = list()
# folders with data to be processed
filelist += ['hover','swipeleft','swiperight']

# n refers to each sensor
for n in range (5):
	# write files one sensor at a time
	f = open("sensor" + str(n+1) + ".txt", "w")
	for folder in filelist:
		# for using modulus
		if (n == 5):
			n = 0
		
		# a refers to the number of text files
		for a in range (1,101):
			# read each file
			r = open(folder + '/stream_' + str(a) + '.txt', "r")
			for i in range(5):
				text = r.readline()
				# only write lines that refer to the designated sensor
				if (i % 5 == n):
					f.write(text)

			r.close()

	f.close()
