#denovo assembly from pacbio long reads
canu -p my_mi -d canu_mi genomeSize=210m useGrid=false maxThreads=64 maxMemory=500g corOutCoverage=200 "batOptions=-dg 3 -db 3 -dr 1 -ca 500 -cp 50"  -pacbio-raw Mi_Pacbio.fasta

canu -p my_mj -d canu_mj genomeSize=280m useGrid=false maxThreads=64 maxMemory=500g corOutCoverage=200 "batOptions=-dg 3 -db 3 -dr 1 -ca 500 -cp 50"  -pacbio-raw Mj_PacBio.fasta

canu -p my_ma -d canu_ma genomeSize=280m useGrid=false maxThreads=64 maxMemory=500g corOutCoverage=200 "batOptions=-dg 3 -db 3 -dr 1 -ca 500 -cp 50"  -pacbio-raw Ma_Pacbio.fasta

canu -p my_mp -d canu_mp genomeSize=210m useGrid=false maxThreads=64 maxMemory=500g corOutCoverage=200 "batOptions=-dg 3 -db 3 -dr 1 -ca 500 -cp 50"  -pacbio-raw Mp_Pacbio.fasta

smartdenovo.pl -c 1 Mg_Pacbio.fasta > wtasm.mak
make -f wtasm.mak
