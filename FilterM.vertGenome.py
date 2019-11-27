file = open("Mortierella_verticillata_NRRL_6337.fasta", "r")
lines = file.readlines()
file.close()

out = open("M_verticillata_NRRL_6337.fasta", "w")
for i, line in enumerate(lines):
    if line [0] == ">" and line[1] == "K":
        seq = 1
    elif line [0] == ">" and line[1] == "A":
        seq = 0

    if seq == 1:
        out.write(line)
