#This scripts iterates through the folder containing alignment (.bam) files and creates pseudo-reference
#	To run:
#		cd /folder with bams/
#		bash make_pseudo_assembly.sh

#loading modules 
module load bioinfo-tools bcftools

#iterates through folder and performs: SNPcalling (mpileup + bcftools call), transformation bam to fasta, using vcf file information 
for d in *bam ; do
    echo "$d"
    bcftools mpileup -Ov -f /proj/uppstore2017185/b2014034_nobackup/Dasha/RAD_Vanessa/4_PopulationAnalysis/mtDNA/GCA_905220365.1_ilVanCard2.1_genomic.mitochondion.fa $d | bcftools call -c -Ov | vcfutils.pl vcf2fq > $d.fasta
done
