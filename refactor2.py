def main():
	f = open("mostVariables.txt", "r")

	lines = []
	line = f.readline()
	counter = 0
	variables = {}
	tempString = ""

	while(line != ""):
		for i in line:
			if i == " " or i == ";":
				counter += 1
			elif counter == 2:
				tempString += i
			
		
		variables[tempString] = []
		tempString = ""
		counter = 0
		line = f.readline()

	f = open("code.txt", "r")
	line = f.readline()

	previousClass = []
	while(line != ""):
		if "{" in line and ("public" in line or "private" in line):
			if "if" not in line and "REQUIRED_PERMISSION_LIST" not in line:
				previousClass.append(line)
				isIfStatement = False
			else:
				isIfStatement = True
		if "}" in line and len(previousClass) > 1 and not isIfStatement:
			previousClass.pop()


		for key in variables:
			if key in line and len(previousClass) >0:
				variables[key].append(previousClass[len(previousClass)-1])
		line = f.readline()

	

	f2 = open("output2.txt", "w+")

	newDict = {}
	for key in variables:
		newDict[key] = []
		for i in variables[key]:
			for each in variables:
				if i in variables[each] and each != key:
					newDict[key].append(each)

	f2 = open("output.txt", "w+")
	for key in newDict:
		tempString = key, " - ", len(newDict[key])
		print tempString




main()