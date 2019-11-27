#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:50:00 -N MortBlast
cd $PBS_O_WORKDIR

module load ncbi-blast/2.2.30+

blastn -query ExonSeqs.fasta -task blastn -db Genomes/U_ramanniana_db \
-evalue 1e-10 -outfmt 7 -out First_BLAST/Exons_v_U_ramanniana.blast_out

blastn -query ExonSeqs.fasta -task blastn -db Genomes/U_ramanniana_db \
-evalue 1e-10 -outfmt 7 -out First_BLAST/Exons_v_U_ramanniana.blast_out

blastn -query ExonSeqs.fasta -task blastn -db Genomes/U_ramanniana_db \
-evalue 1e-10 -outfmt 7 -out First_BLAST/Exons_v_U_ramanniana.blast_out

blastn -query ExonSeqs.fasta -task blastn -db Genomes/U_ramanniana_db \
-evalue 1e-10 -outfmt 7 -out First_BLAST/Exons_v_U_ramanniana.blast_out
