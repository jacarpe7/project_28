filelist = list()
# folders with data to be processed
filelist += ['demo1','demo2']

# n refers to each sensor number 1 through 9
for n in range (1,10):
	# write files one sensor at a time
	f = open("sensor" + str(n) + ".txt", "w")
	for file in filelist:
		# for using modulus
		if (n == 9):
			n = 0
		
		# a refers to the number of text files
		for a in range (1,11):
			# read each file
			r = open(file + '/stream_' + str(a) + '.txt', "r")
			for i in range(1,10):
				text = r.readline()
				# only write lines that refer to the designated sensor
				if (i % 9 == n):
					f.write(text)

			r.close()

	f.close()
