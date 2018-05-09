###############################################################################
#	Written by Natalie Vande Pol
#	March 17, 2016
#
#	*   command line: python linearize.py [path/filename(s)]
#	*   accepts multiple FASTA formatted documents to linearize sequences
#	*   output written to a new version of the input document(s) in original 
#		file loaction with "_linear" appended to the filename
###############################################################################


import sys, os

filenames = sys.argv[1:]

for argument in filenames:
	raw_reads_file = open(argument, "r")
	all_OTU_seqs = raw_reads_file.readlines()
	raw_reads_file.close()
	
	linear_OTU_seqs = []
	for i, line in enumerate(all_OTU_seqs):
		if line[0] == ">":
			linear_OTU_seqs.extend((all_OTU_seqs[i][1:].strip(), ""))
		else:
			linear_OTU_seqs[-1]+=line.strip()

	output = open(os.path.splitext(argument)[0]+"_linear"+os.path.splitext(argument)[1], "w")
	
	for i, line in enumerate(linear_OTU_seqs):
		if (i % 2 == 0):
			output.write( ">"+line + "\n" + linear_OTU_seqs[i+1] + "\n" )
	output.close()
