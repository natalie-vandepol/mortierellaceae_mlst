#Extract exon locations from gff and use these to extract sequences from fasta
#Michigan State University & UC Riverside
#5.12.15
#Natalie Vande Pol

import os

gffFile = open("Mortierella_elongata_AG-77.Morel1.v1.gff3", "r")
gffData = gffFile.readlines()
gffFile.close()

seqFile = open("Mortierella_elongata_AG-77.Morel1.v1.fasta", "r")
seqData = seqFile.readlines()
seqFile.close()

exon_coords = {}
for line in gffData[1:]:
    if line[0] == "#":
        temp = line.split("_")
        temp2 = temp[1].split(" ")
        scaf_num = temp2[0]
        exon_coords[scaf_num] = {}

    else:
        temp = line.split("\t")
        if temp[2] == "exon":
            start = temp[3]
            stop = temp[4]
            ampsize = int(stop)-int(start)
            if ampsize > 800:
                ID = temp[8].split(";")[0][3:]
                exon_coords[scaf_num][ID] = [start, stop]

output = open("exon_coords", "w")

for scaf in exon_coords.keys():
    output.write("scaffold " + str(scaf) +"\n")
    for id in exon_coords[scaf].keys():
        output.write(str(id)+"\t"+str(exon_coords[scaf][id]) + "\n")
        output.write("\n")

output.close()

scaf_seqs = {}
for i, line in enumerate(seqData):
    if line[0] == ">":
        line = line.strip("\n")
        temp = line.split("_")
        scaffold = temp[1]
        scaf_seqs[scaffold] = ""
    else:
        line = line.strip("\n")
        scaf_seqs[scaffold] += line

output2 = open("scaf_seqs", "w")
for num in scaf_seqs.keys():
    output2.write(str(num)+"\n"+scaf_seqs[num]+"\n")
output2.close()

exon_seqs = {}
for scaf_num in exon_coords.keys():
    for id in exon_coords[scaf_num].keys():
        start = int(exon_coords[scaf_num][id][0])
        stop = int(exon_coords[scaf_num][id][1])
        exon_id = id +"_scaf"+scaf_num+"_"+str(start)+"-"+str(stop)
        exon_seqs[exon_id] = scaf_seqs[scaf_num][start-1:stop-1]

output3 = open("ExonSeqs.fasta", "w")
for ex_id in exon_seqs.keys():
    output3.write(">"+ex_id+"\n"+exon_seqs[ex_id]+"\n")

output3.close()
