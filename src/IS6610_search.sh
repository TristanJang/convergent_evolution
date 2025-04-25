#!/bin/bash

for seq in $(cat /home/nthosar9846/assembly/flye/iselements.txt)
do
blastn -subject /home/nthosar9846/assembly/flye/insertion-seqs/sequences/$seq -query /grp/valafar/data/depot/assembly/south_africa/genomes/A12_B180_FV_New.fasta -outfmt "6 pident length qstart qend" > /grp/valafar/data/depot/assembly/south_africa/blast/$seq-A12_FV.aln
done



