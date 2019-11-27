input = open("partitions_codons.txt", "U")
all_lines = input.readlines()
input.close()


for i, line in enumerate(all_lines[1:]):
	temp = line.strip().split("\t")
	locus = temp[0]
	codon1 = temp[1]
	length = temp[2]
	gblocks = temp[3:]

	output = open(locus+"_partition_finder.cfg", "w")
	output.write("# ALIGNMENT FILE # \nalignment = "+locus+".phylip;\n\n# BRANCHLENGTHS #\n\
branchlengths = linked;\n\n\
# MODELS OF EVOLUTION #\n\
models = all;\n\
model_selection = aicc;\n\n\
# DATA BLOCKS #\n\
[data_blocks]\n")

	if codon1=="1":
		pos = [0,1,2,0,1,2,0,1,2]

	if codon1=="2":
		pos = [2,0,1,2,0,1,2,0,1]

	if codon1=="3":
		pos = [1,2,0,1,2,0,1,2,0]

	new_end=0
	j=0
	for m, chunk in enumerate(gblocks):
		tmp2 = chunk[1:-1].split()
		start = int(tmp2[0])
		#shift =1 means there is one more base than full codons
		#shift =2 means there are two more bases than codons
		shift = start%3 - 1

		new_start = new_end+1
		end = int(tmp2[1])
		len = end-start
		new_end = new_start+len

		j+=shift

		output.write("block"+str(m+1)+"_codon1 = "+str(pos[j]+new_start)+"-"+str(new_end)+"/3;\n")
		output.write("block"+str(m+1)+"_codon2 = "+str(pos[j+1]+new_start)+"-"+str(new_end)+"/3;\n")
		output.write("block"+str(m+1)+"_codon3 = "+str(pos[j+2]+new_start)+"-"+str(new_end)+"/3;\n\n")
	output.write("# SCHEMES #\n[schemes]\nsearch = greedy;\n\n# user schemes")
	output.close()