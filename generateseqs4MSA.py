import ConstructMSAinput, sys

filename = sys.argv[1]
exonfile = open(filename, "r")
exons = exonfile.readlines()
exonfile.close()

for i, line in enumerate(exons):
    line = line.strip()
    ConstructMSAinput(line)