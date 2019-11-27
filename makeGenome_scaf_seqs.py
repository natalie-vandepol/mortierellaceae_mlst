def make_scaf_seqs(genome):
    genome_file = open("Genomes/"+genome, "r")
    genome_lines = genome_file.readlines()
    genome_file.close()

    scaf_seqs = {}
    for i, line in enumerate(genome_lines):
        if line[0] == ">":
            line = line.strip("\n")
            temp = line.split(" ")
            scaffold = temp[0]
            scaf_seqs[scaffold] = ""
        else:
            line = line.strip("\n")
            scaf_seqs[scaffold] += line

    genome = genome.split("/")
    genome = genome[1].split("_")
    genome = genome[0][0]+"_"+genome[1]
    output2 = open(genome+"_scaf_seqs.fasta", "w")
    for key in scaf_seqs.keys():
        output2.write(key+"\n"+scaf_seqs[key]+"\n")
    output2.close()


make_scaf_seqs("M_verticillata_NRRL_6337.fasta")
make_scaf_seqs("Mortierella_alpina_B6842.fasta")
make_scaf_seqs("Umbelopsis_isabellina_B7317.fasta")
make_scaf_seqs("Umbelopsis_ramanniana.Umbra1.v1.fasta")

