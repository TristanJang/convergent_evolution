from Bio import SeqIO

# Parse the FASTA file
fasta_file = "/grp/valafar/data/depot/assembly/south_africa/genomes/A12_B180_FV_New.fasta"
records = SeqIO.parse(fasta_file, "fasta")

record = next(records)

sequence = record.seq[1308300:1308600]

#for i in range(len(sequence)):
print(sequence)
