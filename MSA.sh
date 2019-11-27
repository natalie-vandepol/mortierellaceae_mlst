#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:03:00 -N MortBlast
cd $PBS_O_WORKDIR



for file in MSA/*.fasta
do
    name=${file##*/}
    base=${name%.txt}
    muscle -in "$file" -out "MSA/OUT/${base}_muscleOUT.fasta" -clw
done