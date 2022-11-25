##Using kmc, genomescope and smudgeplot to estimate genome size and ploidy

i=$1 ## filelist contain reads file

module load KMC/3.2.1-GCC-11.2.0

mkdir ${i/.filelist/_tmp}

echo kmc -k21 -t16 -m64 -ci1 -fm -cs10000 @${i} ${i/.filelist/_k21} ${i/.filelist/_tmp}

kmc -k21 -t16 -m64 -ci1 -cs10000 -fm @${i} ${i/.filelist/_k21} ${i/.filelist/_tmp}

echo kmc_tools transform ${i/.filelist/_k21} histogram ${i/.filelist/_k21}.hist -cx10000

kmc_tools transform ${i/.filelist/_k21} histogram ${i/.filelist/_k21}.hist -cx10000

module purge

L=$(/beegfs/home/xcs/tools/smudgeplot/bin/smudgeplot.py cutoff ${i/.filelist/_k21}.hist L)

U=$(/beegfs/home/xcs/tools/smudgeplot/bin/smudgeplot.py cutoff ${i/.filelist/_k21}.hist U)

module load KMC/3.2.1-GCC-11.2.0

echo kmc_tools transform ${i/.filelist/_k21} -ci"$L" -cx"$U" dump -s ${i/.filelist/_k21}_L"$L"_U"$U".dump

kmc_tools transform ${i/.filelist/_k21} -ci"$L" -cx"$U" dump -s ${i/.filelist/_k21}_L"$L"_U"$U".dump

module purge

/beegfs/home/xcs/Revision/tools/smudgeplot/bin/smudgeplot.py hetkmers -o ${i/.filelist/_k21}_L"$L"_U"$U" < ${i/.filelist/_k21}_L"$L"_U"$U".dump

## Using genomescope
~/tools/genomescope2.0/genomescope.R -i histfile -k 21 -p 3 -o Mi_genomescope
## Using smudgeplot
~/tools/smudgeplot/smudgeplot.py plot -o OUTFILE coverage.tsv.file

