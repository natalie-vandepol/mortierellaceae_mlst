import sys

filenames = sys.argv[1:]

all_loci = {'locus_ITS':"", 'no_hits':"", 'locus_5512':"", 'locus_370':"", 'locus_1870':"", 'locus_2175':"", 'locus_2451':"", 'locus_4121':"", 'locus_4955':"", 'locus_5401':"", 'locus_5491':"", 'locus_10927':"", 'locus_EF1a':"", 'locus_RPB1':"", 'locus_615':""}

for file in filenames:
	name = file.split("_BLAST")[0]
	fasta = open("../PAIR-assembled/"+name+"/contigs.fasta", "r")
	all_seqs = fasta.readlines()

	seq_dict = {}
	for i, line in enumerate(all_seqs):
		if line.startswith(">"):
			seq_id = line.strip()[1:]
			seq_dict[seq_id]=""
		else:
			seq_dict[seq_id] += line
	fasta.close()
	
	blast = open(file, "r")
	all_hits = blast.readlines()
	for i, line in enumerate(all_hits):
		if line.startswith("Query="):
			temp = line.split()
			seq_ID = temp[1]

		if line.startswith("*****"):
			all_loci['no_hits'] += ">"+name+"__"+seq_ID+"\n"+seq_dict[seq_ID]+"\n"
			
		if line.startswith("Sequences producing"):
			temp2 = all_hits[i+2]
			temp3 = temp2.split()[0].split("_")[0]
			for key in all_loci.keys():
				if temp3 in key:
					all_loci[key] += ">"+name+"__"+seq_ID+"\n"+seq_dict[seq_ID]+"\n"
	blast.close


for key in all_loci.keys():
	output = open(key+".fas", "w")
	count = all_loci[key].count(">")
	print key+"\t"+str(count)
	output.write(all_loci[key])
	output.close()