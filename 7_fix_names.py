import sys

all_filenames = sys.argv[1:]

name_file = open("names.txt", "U")
all_names = name_file.readlines()
name_file.close()
name_dict = {}
for i, line in enumerate(all_names):
	temp0 = line.split()
	name = temp0[0].split("_S")[0]
	name_dict[name] = temp0[1]

for file in all_filenames:
	input = open(file, "U")
	all_lines = input.readlines()
	input.close()

	output = open(file.split(".")[0]+"_taxa.fasta", "w")
	unique_names={}
	for i, line in enumerate(all_lines):
		if line[0] == ">":
			temp1 = line[1:].split("|")[0].split("_S")
			
			seq_ID = temp1[0]
			seq_ID=seq_ID.replace("-", "")
			
			if seq_ID=="KOD48":
				seq_ID="KOD948"
			if seq_ID=="CSDSO235":
				seq_ID="CSDSO2235"
			if seq_ID not in unique_names.keys():
				unique_names[seq_ID]=1
			else:
				unique_names[seq_ID]=unique_names[seq_ID]+1

			output.write(">"+name_dict[seq_ID]+"_"+seq_ID)
			if unique_names[seq_ID]>1:
				output.write("_"+str(unique_names[seq_ID])+"\n")
			else:
				output.write("\n")
			j = i+1
			while j<=(len(all_lines)-1) and all_lines[j][0] != ">":
				output.write(all_lines[j])
				j+=1
	output.close()