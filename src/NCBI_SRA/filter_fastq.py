import subprocess


def count_reads_fastq(file_path):
    # Use grep to count lines starting with "@" and return the count
    result = subprocess.run(['grep', '-c', '^@', file_path], capture_output=True, text=True)
    count = int(result.stdout.strip())
    return count


def filter_fastq_files(input_file, output_file, min_reads=5000):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            fastq_file = line.strip()
            fastq_file = fastq_file + ".fastq"
            if fastq_file:  # Ensure the line is not empty
                read_count = count_reads_fastq(fastq_file)
                if read_count >= min_reads:
                    fastq_file = fastq_file[:-6]
                    outfile.write(fastq_file + '\n')


# Example usage
input_txt = 'SRR_Acc_List_Pacbio.txt'  # Text file containing list of FASTQ files
output_txt = 'filtered_fastq_files.txt'  # Output text file for files with at least 5000 reads
filter_fastq_files(input_txt, output_txt)
