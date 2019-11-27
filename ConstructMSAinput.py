import os, sys

def extract_seq(species):
    blastFile = open("GoodHits_Exons_v_"+species+".blast_out.txt", "r")
    blastData = blastFile.readlines()
    blastFile.close()

    species_file = open(species+"_scaf_seqs.fasta", "r")
    species_lines = species_file.readlines()
    species_file.close()

    exID = "exon_"+exon
    for i, line in enumerate(blastData):
        if line[0] == "e":
            temp = line.split("\t")
            temp2 = temp[0].split("_")
            query = "_".join([temp2[0:2]])
            if query == exID:
                subject = temp[1]
                start = temp[11]
                stop = temp[12]
                query_coords = [q_start, q_stop]
                subj_coords  = [s_start, s_stop]

    for i, line in enumerate(species_lines):
        line = line.strip("\n")
        if line[0] == ">" and line[1:] == scaffold:
            output.write(line+"\n"+species_lines[i+1][start-11:stop+9]+"\n")
#---------------------------------------------------------------------------


exon = sys.argv[1]
exon_seq_file = open("ExonSeqs.fasta", "r")
exons_seq_lines = exon_seq_file.readlines()
exon_seq_file.close()

output = open(exon+"MSA.fasta", "w")

for i, line in enumerate(exons_seq_lines):
    temp = line[1:].split("_")
    ex_ID = "_".join(str(temp[1:2]))
    if ex_ID == exon:
        output.write(line+"\n"+exons_seq_lines[i+1])

extract_seq("M_verticillata")
extract_seq("M_alpina")
extract_seq("U_isabellina")
extract_seq("U_ramanniana")

output.close()
