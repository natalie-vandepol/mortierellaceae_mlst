import os
from os import listdir

directory = os.listdir('.')
all_phylip_files = [x for i, x in enumerate(directory) if x.endswith(".phylip")]

output2 = open("phylip_summary.txt", "w")
for file in all_phylip_files:
	input = open(file, "r")
	all_lines = input.readlines()
	input.close()

	output = open(file.split(".")[0]+".fasta", "w")
	output2.write(file+"\t"+all_lines[0])
	for i, line in enumerate(all_lines[1:]):
		temp = line.split()
		output.write(">"+temp[0]+"\n"+temp[1]+"\n")
	output.close()
output2.close()