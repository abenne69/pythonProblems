def main():
	f = open("output-mostrecent.txt", "r")
	line = f.readline()

	previousClass = []
	while(line != ""):
		if "telemetry" in line.lower():
			previousClass.append(line) 
		line = f.readline()

	f2 = open("output-telemetryNames", "w+")
	for key in previousClass:
		f2.write(key)
main()