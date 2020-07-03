casos = input()
lines = list()


for i in range(int(casos)):
	line = input()
	lines.append(line)

for i in lines:
	size = i.split()
	M = int(size[0])
	N = int(size[1])

	if N >= M:
		if M%2 == 0:
			print("L")
		else:
			print("R")
	else:
		if N%2 == 0:
			print("U")
		else:
			print("D")