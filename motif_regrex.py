#!/usr/bin/env python3

from Bio import SeqIO
import re
import sys
import os.path

infile ="len56seq.fasta"
#number of matches found in sequence
matches=()
#place in sequence where match was found
start = 0
end = 0
#sequence from fasta file
seq = []
#accession number
acc = []
#
found = []
motifs = ['a', 'b', 'c', 'd', 'e']
#goes through each record in the fasta file
for record in SeqIO.parse(infile, "fasta"):
	seq = record.seq
	acc = record.description
	#make list of 0's the same length as protein sequence
	matches = list("0" * (len(record.seq)))
	#print(len(matches))
	#motif 1 regex search
	a = re.finditer(r'[DG]F.DSY', str(seq))
	for match in a:
		start = match.start()
		end = match.end()
		#replace match site in list of 0's with motif number found
		matches[start:end] = (len(matches[start:end])) * ["1"]
		found.append('a')
	#motif 2
	b = re.finditer(r'[LVI][LT][QRE][DN][DE].G', str(seq))
	for match in b:
		start = match.start()
		end = match.end()
		matches[start:end] = (len(matches[start:end])) * ["2"]	
		found.append('b')
	#motif 3
	c = re.finditer(r'[DE][FCV][EG][VIY][LIV][YV]G', str(seq))
	for match in c:
		start = match.start()
		end = match.end()
		matches[start:end] = (len(matches[start:end])) * ["3"]
		found.append('c')
	#motif 4
	d = re.finditer(r'[NMS][TINV].[DH][EQN]', str(seq))
	for match in d:
		start = match.start()
		end = match.end()
		matches[start:end] = (len(matches[start:end])) * ["4"]
		found.append('d')
	#motif 5
	e = re.finditer(r'I[ILV][KIH][LWM]', str(seq))
	for match in e:
		start = match.start()
		end = match.end()
		matches[start:end] = (len(matches[start:end])) * ["5"]
		found.append('e')
		
	
	if matches != list("0" * (len(record.seq))):
		matches = "".join(matches)
		print(">" + str(acc) + "\n" + str(seq) + "\n" + str(matches) + "\n")
			 f.write(record.description)
			 f.write("\n")
			 f.write(str(seq))
			 f.write("\n")
			 f.write(str(matches))
			 f.write("\n")
	#to check for any records that match any motif by coparing the motif list with the found list
	#and add them to a new file in a fasta format with a string of 0's replaced with the number of
	#motifs matching underneath the sequence
	if sum(f in motifs for f in found) == 1:
		print(record.description, found)
		with open('30_40GC_MOTIFres.txt', 'a') as f:
			f.write(acc)
			f.write("\n")
			f.write(str(seq))
			f.write("\n")
			f.write(str(matches))
			f.write("\n")
        #Clear each list for loop restart
	start = 0
	end = 0
	matches = ()
	seq = []
	acc = []
	found = []
	
f.close()
	


        
