


for n in range (1,5):
	f = open("sensor" + str(n) + ".txt", "w")

	if (n == 4):
		n = 0

	r = open("output-fullactivity.txt", "r")
	for i in range(1,801):
		text = r.readline()
		if (i % 4 == n):
			f.write(text)

	r.close()

	r = open("output-leftswipe.txt", "r")
	for i in range(1,801):
		text = r.readline()
		if (i % 4 == n):
			f.write(text)

	r.close()

	r = open("output-null.txt", "r")
	for i in range(1,801):
		text = r.readline()
		if (i % 4 == n):
			f.write(text)

	r.close()

	r = open("output-rightswipe.txt", "r")
	for i in range(1,801):
		text = r.readline()
		if (i % 4 == n):
			f.write(text)

	r.close()

	f.close()

