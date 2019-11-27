
##
# Return a dict with seq id as key, seq as value. Will convert things to
# UNIX format without "\r".
# 
# @param fasta
# @param desc    include desc[1] or not[0,default]. The description is
#                separated from seq id with a space. If include, it will
#                be the first element of the list, the second will be seq
# @param verbose display line count [1], or not [0, default]
# @param dflag   delimit by space or not, default no
# @param newline rid of new line or not
##
def fasta_to_dict(fasta,dflag=0,verbose=0,newline=0):

	# each idx should only occur once.
	inp		= open(fasta,"r")
	inl = inp.readline()
	fdict	= {} # idx as key, seq as value
	c = 0
	N = 0
	while inl != "":
		inl = inl.strip()
		next = 0
		idx	= ""
		desc = ""
		if inl == "":
			pass
		elif inl[0] == ">":
			if verbose and c%1e3 == 0:
				print " %i k" % (c/1e3)
			c += 1
			# rid of anything after space if asked
			if dflag and inl.find(" ") != -1:
				desc = idx[idx.find(" ")+1:]
				idx = idx[:idx.find(" ")]
			else:
				idx = inl[1:]
			# count lines and store seq into a list
			slist = []
			inl = inp.readline()
			while inl[0] != ">":
				inl = inl.strip()
				# Add new line char, do this after strip because I do not
				# want to have cases of /r/n
				if newline:
					inl = inl + "\n"
				slist.append(inl)
				inl = inp.readline()
				if inl == "":
					break
			seq = "".join(slist)

			if fdict.has_key(idx):
				if verbose:
					print "Redundant_id:",idx,
				if dflag:
					if len(fdict[idx][1]) < len(seq):
						fdict[idx] = [desc,seq]
						if verbose:
							print "longer"
					else:
						if verbose:
							print "shorter"
				else:
					if len(fdict[idx]) < len(seq):
						fdict[idx] = seq
					if verbose:
							print "longer"
					else:
						if verbose:
							print "shorter"
			else:
				N += 1
				if dflag:
					fdict[idx] = [desc,seq]
				else:
					fdict[idx] = seq
			next = 1

		# so no extra line is read, because of the innder while
		if not next:
			inl = inp.readline()
	inp.close()
	if verbose:
		print "Total %i sequences, %i with non-redun names" % (c,N)

	return fdict

def dict_to_fasta(fdict,fname):
	oup = open(fname,"w")
	for i in fdict:
		oup.write(">%s\n" % i)
		s = fdict[i]
		c = 0
		while c < len(s):
			oup.write("%s\n" % s[c:c+80])
			c += 80
	oup.close()

# @param fasta  can have multiple sequences in one file
# @param coords [seq][L1,R1,L2,R2...]. If L > R, take reverse complement.
# @param seqid  Use 4th column of the coords file as sequence ID if available.
#               (1) or not (0, default)
def get_stretch4(fasta,coords,seqid=0):
	print "Sequence to dict..."
	seq = fasta_to_dict(fasta,0)
	# fasta_to_dict got rid of "\n" already
	#print seq.keys()
	c = 0 # count total
	m = 0 # count not in fasta
	if coords.find(",") == -1:
		print "Read coordinates..."
		inp = open(coords)
		oup = open(coords+".fa","w")
		inl = inp.readline()
		while inl != "":		# Go through each coord
			if c % 1000 == 0:
				print " %i k" % (c/1000)
			
			L	= inl.strip().split("\t")
			if len(L) == 3:
				c += 1
				print " ",c,L[0],L[1],L[2]
				
			seqName = L[0]	# Sequnece name
			if seqName in seq:
				if len(L) >= 2:
					# L = [name, L, R], some may have 4th col which is IDs to be given.
					if L[1].find(",") == -1:
						# Deal with reverse ori
						ori= 1; cL = int(L[1]); cR = int(L[2])
						if cL > cR:
							ori = -1
						# Get sequence
						if ori == -1:
							S = seq[seqName][cR-1:cL]
						else:
							S = seq[seqName][cL-1:cR]

						if S == "":
							print "ERR COORD: %s,[%i,%i]" % (seqName,cL,cR)
						else:
							if ori == -1:
								S = trans.rc(S)
							# If there is 4th column, use them as sequence IDs.
							if len(L) == 4 and seqid:
								oup.write(">%s\n%s\n" % (L[3],S))
							else:
								oup.write(">%s|%i-%i\n%s\n" % (seqName,cL,cR,S))
					# name <\t> "L1,R1,L2,R2..." <\t> whatever
					elif L[1].find(",") != -1:
						coordList = L[1].split(",")
						S = ""
						# Set orientation, only consider the first pair
						if int(coordList[0]) < int(coordList[1]):
							ori = 1
						else:
							ori = -1
						for j in range(0,len(coordList),2):
							cL = int(coordList[j]); cR = int(coordList[j+1])
							if ori == -1:
								cL = int(coordList[j+1])
								cR = int(coordList[j])
								S = seq[seqName][cL-1:cR] + S
							else:
								S += seq[seqName][cL-1:cR]
						oup.write(">%s|%s\n%s\n" % (seqName,"-".join(coordList),S))
					else:
						print "Unknown cooord format:",L
						print "Quit!"
						sys.exit(0)

			else:
				if seqName != "":
					m += 1
					print "    seq name not found: %s" % seqName
			inl = inp.readline()

		print "Total coords:",c
		print "Not in %s: %i" % (fasta,m)

	# coordinates are passed
	else:
		coords = coords.split(",")
		print "Coords:",coords
		oup = open("%s_%s.fa" % (fasta,"-".join(coords)),"w")
		C = []
		for i in coords:
			C.append(int(i))
		for i in seq:
			s = ""
			for j in range(0,len(C),2):
				s += seq[i][C[j]-1:C[j+1]]
			oup.write(">%s\n%s\n" % (i,s))

	print "Output fasta file: %s.fa" % coord
	oup.close()
	print "Done!"

def check_fasta(fasta):
	try:
		inl = open(fasta).readlines()
	except IOError:
		print "\n%s is not found!\n" % fasta
		help()
	is_fasta = 0
	for i in inl:
		if i[0] == ">":
			is_fasta = 1
	return is_fasta

def check_coord(coord):
	try:
		inl = open(coord).readline()
	except IOError:
		print "\n%s is not found!\n" % coord
		help()
	is_coord = 0
	L = inl.split("\t")
	if len(L) == 3:
		is_coord = 1
	return is_coord

def help():
	print "\nUsage: python get_fasta_seq.py fasta_file_name coordinate_file_name\n"
	print "  coordinate file: tab delimited with three columns"
	print "      col 1: sequence name, must be the same as that in the fasta file"
	print "      col 2: left coordinate of the domain from HMMER output"
	print "      col 3: right coordinate of the domain from HMMER output\n"
	sys.exit(0)
	
	
#-------------------------------------------------------------------------------

import sys

if len(sys.argv) != 3:
	help()

fasta = sys.argv[1]
coord = sys.argv[2]

is_fasta = check_fasta(fasta)
if not is_fasta:
	print "\n%s is not a fasta file!\n" % fasta
	help()

is_coord = check_coord(coord)
if not is_coord:
	print "\n%s is not a coord file!\n" % coord
	help()

FD = fasta_to_dict(fasta)
#print FD	

get_stretch4(fasta,coord)

