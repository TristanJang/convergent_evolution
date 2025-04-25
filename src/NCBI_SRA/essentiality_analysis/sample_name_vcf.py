import subprocess
isolates = open("/home/tjang8858/assembly/pacbio_sra_single_contig.txt", "r")
for isolate in isolates:
    isolate = isolate.strip()
    command = "cat " + isolate+ "_sniffles.vcf | sed 's/INFO\tFORMAT\tSAMPLE/INFO\tFORMAT\t" +isolate +"/' > " + isolate + "_sample.vcf"
    print(command)
    #subprocess.call(command,shell=True)