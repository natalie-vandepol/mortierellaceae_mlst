def filter_file(filename):
	blastfile = open(filename, "r")
	blastlines = blastfile.readlines()
	blastfile.close()

	exon_hits={}
	for i, line in enumerate(blastlines):
		if line[0] != "#":
			temp = line.split("\t")
			ex_id = temp[0]
			subj_id = temp[1]
			ident = float(temp[2])
			aln_len = int(temp[3])
			bit_score = float(temp[11])
			if ex_id not in exon_hits.keys():
				exon_hits[ex_id] = [1,""]
			else:
				exon_hits[ex_id][0] += 1
			if aln_len > 900:
				exon_hits[ex_id][1] += line
			else: pass
		else: pass

	for exon in exon_hits.keys():
		if exon_hits[exon][0] > 10 or exon_hits[exon][1] == "":
			del exon_hits[exon]

	output = open("GoodHits_"+filename+".txt", "w")
	output.write("# Total Exons: %u \n" % len(exon_hits))
	output.write("# Fields: query\tsubject\tpercent identity\talignment len mismatches\
              \tgap opens\tq. start\tq. end\ts. start\ts. end\tevalue\tbit score\n")

	for exID in exon_hits.keys():
		output.write(exon_hits[exID][1])
		output.write("\n")

	output.close()
	return exon_hits

Malpi_hits = filter_file("Exons_v_M_alpina.blast_out")
Mvert_hits = filter_file("Exons_v_M_verticillata.blast_out")
#Uisab_hits = filter_file("Exons_v_U_isabellina.blast_out")
#Urama_hits = filter_file("Exons_v_U_ramanniana.blast_out")

inBothMort = []
for key in Mvert_hits.keys():
	if key in Malpi_hits.keys():
		inBothMort.append(key)
inBothMort.sort()

#inAll = []
#for key in inBothMort:
#	if key in Uisab_hits.keys() and key in Urama_hits.keys():
#		inAll.append(key)
#inAll.sort()

exon_seqs_file = open("ExonSeqs.fasta", "r")
exon_seqs_lines = exon_seqs_file.readlines()
exon_seqs_file.close()

exon_seqs = {}
for i, line in enumerate(exon_seqs_lines):
	if line[0] == ">":
		key = line[1:].strip()
		exon_seqs[key]=""
	elif line != "\n":
		exon_seqs[key] += line

output2 = open("ExonsIn_ALLMort_%u.fasta" % len(inBothMort), "w")
for key in inBothMort:
	output2.write("\n"+"\n".join([">"+key, exon_seqs[key]]))
output2.close()

#output3 = open("ExonsIn_ALL_%u.fasta" % len(inAll), "w")
#for key in inAll:
#	output3.write("\n"+"\n".join([">"+key, exon_seqs[key]]))
#output3.close()