#PBS -l nodes=1:ppn=8,mem=16gb,walltime=01:59:00 -N PAIR_BLAST
cd $PBS_O_WORKDIR


module load  BLAST+


makeblastdb -in All_MLST_Exons.fas -dbtype nucl -out database2/Exons_db -parse_seqids

for file in REV-phix/*.fastq
do
    name=${file##*/}
	base=${name%_R2.fastq}
	blastn -query PAIR-assembled/${base}/contigs.fasta -db database2/Exons_db \
	-out PAIR_BLAST/${base}_BLAST.txt
done
