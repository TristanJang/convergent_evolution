import argparse
import os
import gzip

parser = argparse.ArgumentParser(description='Searches VCF files for structural variants overlapping target genes')
parser.add_argument('-i', '--isfile', help='Name of input file with Isolate IDs',
                    default='isolates-nrd-has-pbhoover-depot.txt')
parser.add_argument('-o', '--outfile', help='Name of output file to write',
                    default='svs-overlapping-candidate-genes.txt')
parser.add_argument('-g', '--genefile', help='Name of input file with positions of target genes',
                     default='candidate-gene-regions.csv')
parser.add_argument('-d', '--isdir',
                    help='Name of director with input vcf files. Excpecsts VCS files in directory to be named {Isolate ID}.vcf',
                    default='isolates')
args = parser.parse_args()


with open(args.isfile, 'r') as f:
    isolatelines = f.readlines()

with open(args.genefile, 'r') as f:
        generegionlines = f.readlines()
genestarts = {}
genestops = {}
for line in generegionlines:
    linebits = line.strip('\n').split(',')
    genestarts[linebits[0]]=int(linebits[1])
    genestops[linebits[0]]=int(linebits[2])


with open(args.outfile, 'w') as f:
    f.write('Isolate\tGene\tGeneStart\tGeneStop\tSVStart\tSVStop\tSVLen\tSVType\tVariant\n')

for isolate in isolatelines:
    isolate = isolate.strip('\n')
    vcf = args.isdir + '/' + isolate + '.vcf'
    if os.path.isfile(vcf):
        with open(vcf, 'r') as f:
            vcflines = f.readlines()
    else:
        vcfgz = vcf + '.gz'
        if os.path.isfile(vcfgz):
            with gzip.open(vcfgz, 'rt') as f:
                vcflines = f.readlines()
        else:
            print(vcf + ' does not exist')
            continue

    matchinglines = []
    for line in vcflines:
        if not line.startswith('#'):
            sv_start = int(line.split('\t')[1])

            infocolumn = line.split('\t')[7]
            sv_type = infocolumn.split('SVTYPE=')[1]
            if 'BND' in sv_type:
                continue

            if ';' in sv_type:
                sv_type = sv_type.split(';')[0]

            sv_end = infocolumn.split('END=')[1]
            if ';' in sv_end:
                sv_end = int(sv_end.split(';')[0])
            else:
                sv_end = int(sv_end)

            sv_len = sv_end - sv_start
            # std_start = infocolumn.split('STD_quant_start=')[1].split(';')[0]
            # std_stop = infocolumn.split('STD_quant_stop=')[1].split(';')[0]
            # sv_rnames = infocolumn.split('RNAMES=')[1].split(';')[0]
            for gene in genestarts:
                overlap = 1
                if sv_start < genestarts[gene] and sv_end < genestarts[gene]:
                    overlap = 0
                if sv_start > genestops[gene] and sv_end > genestops[gene]:
                    overlap = 0
                if overlap:
                    matchinfo = [isolate, gene, str(genestarts[gene]),
                                 str(genestops[gene]), str(sv_start),
                                 str(sv_end),str(sv_len),sv_type,line]
                    matchline = '\t'.join(matchinfo)
                    matchinglines.append(matchline)
    if matchinglines:
        with open(args.outfile, 'a') as f:
            f.writelines(matchinglines)

