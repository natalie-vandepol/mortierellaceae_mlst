import os, sys

def extract_seq(species):
	species_file = open("../../"+species+"_scaf_seqs.fasta", "r")
	species_lines = species_file.readlines()
	species_file.close()

	for scafID in all_hits[species].keys():
		temp = scafID.split(".")
		scaffold = temp[0]
		start = min(all_hits[species][scafID])
		stop = max(all_hits[species][scafID])
		seqID = scafID+"_"+str(start)+"_"+str(stop)
		for i, line in enumerate(species_lines):
			line = line.strip()
			if line[0] == ">" and line[1:] == scaffold:
				output.write(line+"\n"+species_lines[i+1][start-19:stop+20]+"\n")
#---------------------------------------------------------------------------

results_filename = sys.argv[1]
results_file = open(results_filename+".txt", "r")
results = results_file.readlines()
results_file.close()

output = open(results_filename+"_hit_seqs.fasta", "w")

firstline = results[0]
temp = firstline.split()
output.write(">"+temp[0]+"_F\n"+temp[1]+"\n>"+temp[0]+"_R\n"+temp[2]+"\n")

all_hits = {"M_elongata": {}, "M_alpina": {}, "M_verticillata": {}}
for i, hit in enumerate(results[1:]):
	temp = hit.split()
	temp2 = temp[0].split(":")
	scafID = temp2[0]
	if temp[0][0] == "M":
		if scafID in all_hits["M_elongata"].keys():
			scafID+=".2"
		all_hits["M_elongata"][scafID] = [int(temp[4]), int(temp[7])]
	elif temp[0][0] == "A":
		if scafID in all_hits["M_alpina"].keys():
			scafID+=".2"
		all_hits["M_alpina"][scafID] = [int(temp[4]), int(temp[7])]
	else:
		if scafID in all_hits["M_verticillata"].keys():
			scafID+=".2"
		all_hits["M_verticillata"][scafID] = [int(temp[4]), int(temp[7])]

for key in all_hits.keys():
	extract_seq(key)

output.close()
