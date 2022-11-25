import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
seqs=SeqIO.parse(sys.argv[1], "fasta")
seq_dict = {}

for j in seqs:
    seq_dict[str(j.id)] = str(j.seq).upper()

target = str(sys.argv[2])
print(">" + target)
print(dic[target])

   
