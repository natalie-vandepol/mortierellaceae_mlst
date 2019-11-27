#PBS -l nodes=1:ppn=4,mem=1gb,walltime=00:01:00
cd $PBS_O_WORKDIR

module load ncbi-blast/2.2.30+

makeblastdb -in Mucor_circinelloides.Mucci2.v2.fasta -dbtype nucl \
-out databases/Mu_circinelloides_db -parse_seqids

makeblastdb -in Mucor_indicus_B7402.fasta -dbtype nucl \
-out databases/Mu_indicus_db -parse_seqids

makeblastdb -in Mucor_irregularis_B50.fasta -dbtype nucl \
-out databases/Mu_irregularis_db -parse_seqids

makeblastdb -in Mucor_racemosus_B9645.fasta -dbtype nucl \
-out databases/Mu_racemosus_db -parse_seqids

makeblastdb -in Mucor_ramosissimus_97-1192.fasta -dbtype nucl \
-out databases/Mu_ramosissimus_db -parse_seqids

makeblastdb -in Mucor_velutinosus_B5328.fasta -dbtype nucl \
-out databases/Mu_velutinosus_db -parse_seqids

makeblastdb -in Mucormycotina_ATCC_32222.fasta -dbtype nucl \
-out databases/Mumyc_ATCC_32222_db -parse_seqids

makeblastdb -in Mucormycotina_B6842.fasta -dbtype nucl \
-out databases/Mumyc_B6842_db -parse_seqids