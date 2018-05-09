#PBS -l nodes=1:ppn=32,mem=128gb,walltime=04:59:00 -N LOCUS_RE-MUSCLE
cd $PBS_O_WORKDIR


module load muscle

for locus_file in *_muscle.fas
do
	muscle -in ${locus_file} -out ${locus_file}_re-muscle.msa
done