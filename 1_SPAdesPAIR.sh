#PBS -l nodes=1:ppn=8,mem=16gb,walltime=03:59:00 -N SPAdesPAIR
cd $PBS_O_WORKDIR


module load SPAdes/3.7.1

for file in REV-phix/*.fastq
do
    name=${file##*/}
	base=${name%_R2.fastq}
	spades.py -1 FWD-phix/${base}_R1.fastq -2 REV-phix/${name} -o PAIR-assembled/${base}
done
