# locus_name:[length, num_full_length, num_partial]
all_loci = {'locus_ITS':[1800,0,0], 'no_hits':[50,0,0], 'locus_5512':[1600,0,0], 'locus_370':[980,0,0], 'locus_1870':[1700,0,0], 'locus_2175':[1400,0,0], 'locus_2451':[1900,0,0], 'locus_4121':[950,0,0], 'locus_4955':[750,0,0], 'locus_5401':[1400,0,0], 'locus_5491':[940,0,0], 'locus_10927':[2000,0,0], 'locus_EF1a':[1320,0,0], 'locus_RPB1':[1480,0,0], 'locus_615':[1560,0,0]}
all_samples = {}
key_order=['locus_5512', 'locus_370', 'locus_1870', 'locus_2175', 'locus_5491', 'locus_2451', 'locus_4121', 'locus_4955', 'locus_5401', 'locus_EF1a', 'locus_RPB1', 'locus_615', 'locus_10927', 'locus_ITS', 'no_hits']

bad_samples = ["Z69", "AD30", "AD030", "AG69", "AG12", "AG14-9", "C-MNSO23-21", "KSSO1-41", "KSSO2-49"]

for locus in key_order:
	input_file = open(locus+"_linear.fas", "r")
	input = input_file.readlines()
	input_file.close()
	
	output1 = open(locus+"_full.fas", "w")
	min_len = 0.8*all_loci[locus][0]
	for i, line in enumerate(input):
		if line.startswith(">"):
			temp0 = line.split("_S")
			sample_ID = temp0[0][1:]
			if sample_ID not in all_samples.keys():
				all_samples[sample_ID] = {'locus_ITS':[0,0], 'no_hits':[0,0], 'locus_5512':[0,0], 'locus_370':[0,0], 'locus_1870':[0,0], 'locus_2175':[0,0], 'locus_2451':[0,0], 'locus_4121':[0,0], 'locus_4955':[0,0], 'locus_5401':[0,0], 'locus_5491':[0,0], 'locus_10927':[0,0], 'locus_EF1a':[0,0], 'locus_RPB1':[0,0], 'locus_615':[0,0]}
			if len(input[i+1])>=min_len:
				all_samples[sample_ID][locus][0]+=1
				if sample_ID not in bad_samples:
					output1.write(line+input[i+1])
			else:
				all_samples[sample_ID][locus][1]+=1
	output1.close()
			
output = open("MLST_seq_summary.txt", "w")
output.write("Sample\t")
for key in key_order:
	output.write(key+"_full\t"+key+"_partial\t")
output.write("\n")

for sample2 in all_samples.keys():
	output.write(sample2+"\t")
	for key in key_order:
		output.write(str(all_samples[sample2][key][0])+"\t"+str(all_samples[sample2][key][1])+"\t")
	output.write("\n")
output.close()