import sys, getopt, argparse, os.path

def split():
	sys.stdout.write("Starting script excution...\n\n")

	fin = open(inputFile, 'r')
	fout = open(outputFile, 'a')

	linelegth = num(numberBytes)
	totalbytes = 0
	lines = 0

	while True:
		line = fin.read(linelegth)
		if not line:
		 	# sys.stdout.write("End of file\n")
		 	break
		totalbytes = totalbytes + linelegth
		lines = lines + 1

		fout.write(line)
		fout.write("\n")

	sys.stdout.write("Splitted %s bytes in %s lines \n\n" % (totalbytes,lines))
	sys.stdout.write("End excution.\n")

def verifyParameters(argv):

	parser = argparse.ArgumentParser(
		description='Splitter script will split one file in multiple lines')
	parser.add_argument('-i','--inputfile', dest="filename", metavar="STRING", 
	 	help='Input filename, Relative of Full Path', required=True)
	parser.add_argument('-b','--bytes', dest="bytes", metavar="INT",
	 	help='Number of bytes to break each lineline', required=True)
	
	args = vars(parser.parse_args())

	global inputFile
	global outputFile
	global numberBytes

	inputFile = args['filename']
	outputFile = args['filename'] + "-splitted"
	numberBytes = args['bytes']

	print ("Input file is ", inputFile)
	print ("Output file is ", outputFile)
	print ("Number of bytes ", numberBytes)

def is_valid_file(file):
    if not os.path.exists(file):
        print ("The file %s does not exist!" % file)
        sys.exit(2)

def num(s):
    try:
        return int(s)
    except ValueError:
        print ("The value %s is invalid!, Use a integer value" % s)
        sys.exit(3)

def main(argv):
	sys.stdout.write("Python %s \n" % (sys.version))
	verifyParameters(argv)
	is_valid_file(inputFile)
	split()

if __name__ == "__main__":
    main(sys.argv[1:])