import glob, os
#os.chdir("/mydir")

organisms = []
organisms = []
for file in open("files.txt", 'r'):#os.system("ls *.faa | sort -R"):
    file = file.strip()
    organisms.append(file[:len(file)-4])

#print("***********************MAKING DATABASES******************************")
#Python command: makeblastdb -in PA14.txt -out PA14.db

for organism in organisms:
   os.system("makeblastdb -in "+organism+".faa -out "+organism+".db")

print("*****************RUNNING PAIRWISE REVERSE BLAST************************")

#for i in range(len(organisms)):
organism1 = organisms[0]
for j in range(1, len(organisms)):
   #for j in range(17, len(organisms)):
      organism2 = organisms[j]
      #if (organism1 != organism2):
      print ("+++++++++++ RETRIEVING ORTHOLOGS OF "+organism1+" AND "+organism2+" +++++++++++++++")
      #print ("ITERATION: "+str(i)+" "+str(j))
      #x = input()
      #print("blastp -query "+organism1+".faa -db "+organism2+".db -outfmt 6 > "+organism1+"_"+organism2+".txt")
      print("RUNNING FIRST BLASTP...")
      os.system("blastp -query "+organism1+".faa -db "+organism2+".db -outfmt 6 > "+organism1+"_"+organism2+".txt")
      print("RUNNING SECOND BLASTP...")
      os.system("blastp -query "+organism2+".faa -db "+organism1+".db -outfmt 6 > "+organism2+"_"+organism1+".txt")
      print("RECIPROCAL BLAST...")
      os.system("python reciprocal\ blast.py "+organism2+"_"+organism1+".txt "+organism1+"_"+organism2+".txt "+organism1+"_"+organism2+".out")
      print("SCREEN...")
      os.system("python screen_both.py "+organism1+".faa "+organism2+".faa "+organism1+"_"+organism2+".out")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("****************************DONE****************************************")
#blastp -query PA1.txt -db PA14.db -outfmt 6 > PA1_PA14
#blastp -query PA14.txt -db PA1.db -outfmt 6 > PA14_PA1
#python reciprocal\ blast.py PA14_PA1 PA1_PA14 rbb_out




