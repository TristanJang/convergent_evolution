#!/bin/bash
# File with accession numbers, one per line
accession_file="SRR_Acc_List_Pacbio.txt"
# Specify the output directory for the FASTQ files
output_dir="/grp/valafar/data/nihtransfer/sra_pacbio"
# Read the entire file content into a variable
accessions=$(cat "$accession_file")
# Loop through each accession number and download data if not already present
for accession in $accessions; do
    fastq_file="$output_dir/${accession}.fastq"
    if [ -f "$fastq_file" ]; then
        echo "File $fastq_file already exists. Skipping download for $accession."
    else
        echo "Downloading data for $accession..."
        # Use fasterq-dump to download and convert data to FASTQ format
        /home/tjang8858/time_course_BDQ/NCBI_SRA/sratoolkit.3.1.0-centos_linux64/bin/fasterq-dump --outdir "$output_dir" "$accession" --threads 16
    fi
done
echo "Download complete."
