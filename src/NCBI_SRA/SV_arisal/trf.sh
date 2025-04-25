#!/bin/bash

for seq in $(cat /home/tjang8858/time_course_BDQ/NCBI_SRA/SV_arisal/genes.txt)
do
trf /home/tjang8858/time_course_BDQ/NCBI_SRA/SV_arisal/$seq.fasta 2 5 10 80 10 50 2000 -d
done
