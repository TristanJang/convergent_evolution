from Bio import SeqIO

output_fasta = "PE_PGRS_inserted_seq.fasta"
for seq in SeqIO.parse("DRR261202.fasta", "fasta"):
    sequence1 = seq[1633076:1633282]
    print(sequence1)

# Write modified sequences to output FASTA file
with open(output_fasta, "w") as output_handle:
    SeqIO.write(sequence1, output_handle, "fasta")


print("Sequence pull completed. Output saved to", output_fasta)
