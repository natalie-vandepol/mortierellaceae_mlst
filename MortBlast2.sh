#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:03:00 -N MortBlast
cd $PBS_O_WORKDIR

module load ncbi-blast/2.2.30+

blastn -query ExonsIn_ALL_92.fasta -task blastn -db Genomes/U_ramanniana_db \
-evalue 0.0000000001 -outfmt 7 -out SecondBLAST/FilteredExons_ALL_v_U_ramanniana.blast_out

blastn -query ExonsIn_ALL_92.fasta -task blastn -db Genomes/U_isabellina_db \
-evalue 0.0000000001 -outfmt 7 -out SecondBLAST/FilteredExons_ALL_v_U_isabellina.blast_out

blastn -query ExonsIn_ALL_92.fasta -task blastn -db Genomes/M_alpina_db \
-evalue 0.0000000001 -outfmt 7 -out SecondBLAST/FilteredExons_ALL_v_M_alpina.blast_out

blastn -query ExonsIn_ALL_92.fasta -task blastn -db Genomes/M_verticillata_db \
-evalue 0.0000000001 -outfmt 7 -out SecondBLAST/FilteredExons_ALL_v_M_verticillata.blast_out

blastn -query ExonsIn_ALLMort_827.fasta -task blastn -db Genomes/M_alpina_db \
-evalue 0.0000000001 -outfmt 7 -out SecondBLAST/FilteredExons_ALLMort_v_M_alpina.blast_out

blastn -query ExonsIn_ALLMort_827.fasta -task blastn -db Genomes/M_verticillata_db \
-evalue 0.0000000001 -outfmt 7 -out SecondBLAST/FilteredExons_ALLMort_v_M_verticillata.blast_out
