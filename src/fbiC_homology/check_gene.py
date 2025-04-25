from Bio import SeqIO
"""
def delete_bases(sequence, position, length):
    
    Perform deletion of bases in a sequence.

    Args:
    - sequence (str): Input sequence.
    - position (int): Position of the deletion (1-based index).
    - length (int): Length of bases to delete.

    Returns:
    - str: Sequence after deletion.
    
    return sequence[:position - 1] + sequence[position - 1 + length:]


# Input and output filenames
input_fasta = "A12_B180_FV_New.fasta"
output_fasta = "A12_FV_fbiC_deletion.fasta"

# Position and length of deletion
deletion_position = 1308417
deletion_length = 62

# Read input FASTA file
records = list(SeqIO.parse(input_fasta, "fasta"))

# Modify sequence
for record in records:
    if deletion_position <= len(record.seq):
        record.seq = delete_bases(record.seq, deletion_position, deletion_length)
    else:
        print("Deletion position is beyond sequence length.")
"""
output_fasta1 = "fbiC_deletion.fasta"
output_fasta2 = "fbiC_deletion_homology_check.fasta"
for seq in SeqIO.parse("A12_B180_FV_New.fasta", "fasta"):
    sequence1 = seq[1308416:1308478]
    sequence2 = seq[1308478:1308540]
    print(sequence1)
    print(sequence2)

# Write modified sequences to output FASTA file
with open(output_fasta1, "w") as output_handle:
    SeqIO.write(sequence1, output_handle, "fasta")

print("Sequence pull completed. Output saved to", output_fasta1)
# Write modified sequences to output FASTA file
with open(output_fasta2, "w") as output_handle:
    SeqIO.write(sequence2, output_handle, "fasta")

print("Sequence pull completed. Output saved to", output_fasta2)
