from Bio import SeqIO

output_fasta = "H37Rv_fbiC_deletion.fasta"

for seq in SeqIO.parse("H37Rv.fasta", "fasta"):
    sequence1 = seq[1305493:1305693]
    print(sequence1)

# Write modified sequences to output FASTA file
with open(output_fasta, "w") as output_handle:
    SeqIO.write(sequence1, output_handle, "fasta")

print("Sequence pull completed. Output saved to", output_fasta)
