#!/usr/bin/env python3
import argparse
import sys
import mysql.connector
import os.path

dbname   = "phage_db"
dbhost   = "obiwan.cryst.bbk.ac.uk"
dbuser   = "sc001"   
dbpass   = "*******"   
port     = 3306	

#create connection to db
db = mysql.connector.connect(host=dbhost ,port=port,user=dbuser,db=dbname,passwd=dbpass)

#SQL query
p56query ="SELECT genome_accession, gene_ID, AA_seq  FROM genome, protein WHERE accession = genome_accession AND GC_content BETWEEN 30 AND 40 AND protein_PI BETWEEN 1 AND 6 AND genome_size < 40000 AND CHAR_LENGTH(AA_seq) BETWEEN 40 AND 220 GROUP BY AA_seq ORDER BY genome_accession;"


#create cursor and execute
cursor = db.cursor()
cursor.execute(p56query)	
results = cursor.fetchall()

#write output to a file

with open('30_40GC.fasta', 'w') as f:
	for row in results:
		f.write(">" + str(row[0]) + " " + str(row[1]) + "\n" + str(row[2]) + "\n")
		
f.close()

cursor.close()
db.close()
