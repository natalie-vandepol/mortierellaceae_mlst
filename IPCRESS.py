input = open("Primers.txt", "r")
allprimers = input.readlines()
input.close()

for i, line in enumerate(allprimers):
	line = line.strip()
	temp = line.split("\t")
	exon = temp[0]
	Fprimer = temp[1]
	Rprimer = temp[2]
	lo_bound = "50"
	hi_bound = "3500"
	out = "ID"+exon+"\t"+Fprimer+"\t"+Rprimer+"\t"+lo_bound+"\t"+hi_bound

	output = open(exon+".txt", "w")
	output.write(out)
	output.close()