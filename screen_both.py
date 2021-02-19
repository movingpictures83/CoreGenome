import sys
import os

#reference = sys.argv[1]
#os.system("cp "+reference+" "+sys.argv[4])

firstfile = sys.argv[1] #sys.argv[1]
secondfile = sys.argv[2]
thirdfile = sys.argv[3]


seq1 = set()
seq2 = set()

file3 = open(thirdfile, 'r')

for line in file3:
   myline = line.strip()
   seqnames = myline.split('\t')
   seq1.add(seqnames[0])
   seq2.add(seqnames[1])


lines1 = []
file1 = open(firstfile, 'r')
for line in file1:
   myline = line.strip()
   if (myline[0] == '>'):
     #contents = myline.split('\w')
     #myseq = contents[0][1:]
     myseq = myline[1:myline.find(' ')]
     if (myseq in seq1):
       lines1.append(myline)
       lines1.append(file1.readline().strip())

lines2 = []
file2 = open(secondfile, 'r')
for line in file2:
   myline = line.strip()
   if (myline[0] == '>'):
     myseq = myline[1:myline.find(' ')]
     if (myseq in seq2):
        lines2.append(myline)
        lines2.append(file2.readline().strip())

fourthfile = open(firstfile, 'w')
#fifthfile = open(sys.argv[2], 'w')

for line in lines1:
   fourthfile.write(line+"\n")

#for line in lines2:
#   fifthfile.write(line+"\n")




