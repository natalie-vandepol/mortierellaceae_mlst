input = open("RaxML_Partitions.txt", "r")
all_lines = input.readlines()
input.close()

output = open("RaxML_Partitions_Concat.txt", "w")
offset = 0
count = 1
for i, line in enumerate(all_lines):
	if line.startswith("DNA"):
		# line[:11] = "DNA, Subset"
		output.write(line[:11]+str(count)+" = ")
		temp1 = line[15:].strip().split()
		# temp1 = ["1062-1143\3,", "1048-1061\3,", "3-30\3, 1-30\3"]
		for j, item in enumerate(temp1):
			if j< len(temp1)-1:
				temp2 = item[:-3].split("-")
			else:
				temp2 = item[:-2].split("-")
			# temp2 = ["1062", "1143"]
			start = int(temp2[0])
			end   = int(temp2[1])
			new_start = start + offset
			new_end   = end   + offset
			output.write(str(new_start)+"-"+str(new_end)+"\\3")
			if j<len(temp1)-1:
				output.write(", ")
		output.write("\n")
		count+=1
	else:
		temp0 = line.strip().split("-")
		offset = offset+int(temp0[1])
