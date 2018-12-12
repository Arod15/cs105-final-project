f = open("clean_main.csv", "w")
i = 0
with open('Police_Killingsnonumbersyesno.csv', 'r') as csvfile:
	keep_indices = [3, 8, 9, 10, 11, 12]
	# csvfile.readline()
	for x in csvfile:
		line = x.split(",")
		res = []
		for col in range(len(line)):
			if "'" in line[col]:
				line[col] = line[col].replace("'", "")
			# if col in keep_indices:
			# 	res.append(line[col])
		string = ",".join(line)
		print(string[:-1], file=f)
f.close()