def main():
	f = open("code.txt", "r")

	lines = []
	line = f.readline()
	while(line != ""):
		if "private" in line or "public" in line:
			lines.append(line)
		line = f.readline()

	f2 = open("output-mostrecent.txt", "w+")

	for l in lines:
		f2.write(l)

main()