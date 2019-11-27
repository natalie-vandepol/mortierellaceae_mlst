import sys

filename = sys.argv[1]
file = open(filename, "r")
file_lines = file.readlines()
file.close()

exons = {}
for i, line in enumerate(file_lines):
    if line[0] == ">":
        temp = line[1:].split("_")
        gene_num = temp[1]
        exon_num = temp[2]
        temp2 = temp[4].split("-")
        start = temp2[0]
        stop = temp[1]

        if gene_num not in exons.keys():
            exons[gene_num] = {}
        exons[gene_num][exon_num] = [start, stop]

output = open("adjacent_exons_"+filename, "w")
for gene in exons.keys():
    if len(exons[gene])>1:
        t = [int(number) for number in exons[gene].keys()]
        diff = [abs(j-i) for i, j in zip(t[:-1], t[1:])]
        if 1 in diff:
            output.write(gene+"\t"+str(exons[gene].keys())+"\n")
output.close()