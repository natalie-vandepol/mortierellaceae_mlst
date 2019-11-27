#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:03:00 -N MortBlast
cd $PBS_O_WORKDIR

module load muscle
module load python

for file in Processed/*.txt
do
    name=${file##*/}
    base=${name%.txt}
    python extract_ICPRESS_hits ${base}
	muscle -in Processed/${base}_hit_seqs.fasta -out "${base}_hit_MSA.fasta" -clw
done