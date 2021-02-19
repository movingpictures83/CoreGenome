import glob, os
#os.chdir("/mydir")
import PyPluMA

class CoreGenomePlugin:
   def input(self, inputfile):
               self.parameters = dict()
               infile = open(inputfile, 'r')
               for line in infile:
                   print(line)
                   contents = line.strip().split('\t')
                   self.parameters[contents[0]] = contents[1]
               self.organisms = []
               self.fileprefix = PyPluMA.prefix()
               for file in open(self.fileprefix + "/" + self.parameters["fasta"], 'r'):
                  file = file.strip()
                  self.organisms.append(file[:len(file)-4])

   def run(self):
      #print("***********************MAKING DATABASES******************************")
      #Python command: makeblastdb -in PA14.txt -out PA14.db

      for organism in self.organisms:
         if (self.parameters["dbtype"] == "nucleotide"):
            os.system("makeblastdb -in "+self.fileprefix+"/"+organism+".ffn -dbtype nucl -out "+self.fileprefix+"/"+organism+".db")
         else:
            os.system("makeblastdb -in "+self.fileprefix+"/"+organism+".faa -out "+self.fileprefix+"/"+organism+".db")

   def output(self, outputfile):
      print("*****************RUNNING PAIRWISE REVERSE BLAST************************")

      #for i in range(len(organisms)):
      organism1 = self.organisms[0]
      if (self.parameters["dbtype"] == "nucleotide"):
         os.system("cp "+self.fileprefix+"/"+organism1+".ffn "+outputfile)
      else:
         os.system("cp "+self.fileprefix+"/"+organism1+".faa "+outputfile)
      for j in range(1, len(self.organisms)):
         #for j in range(17, len(organisms)):
            organism2 = self.organisms[j]
            #if (organism1 != organism2):
            print ("+++++++++++ RETRIEVING ORTHOLOGS OF "+organism1+" AND "+organism2+" +++++++++++++++")
            #print ("ITERATION: "+str(i)+" "+str(j))
            #x = input()
            #print("blastp -query "+organism1+".faa -db "+organism2+".db -outfmt 6 > "+organism1+"_"+organism2+".txt")
            if (self.parameters["dbtype"] == "nucleotide"):
               print("RUNNING FIRST BLASTN...")
               os.system("blastn -query "+outputfile+" -db "+self.fileprefix+"/"+organism2+".db -outfmt 6 > "+self.fileprefix+"/"+organism1+"_"+organism2+".txt")
               print("RUNNING SECOND BLASTN...")
               os.system("blastn -query "+self.fileprefix+"/"+organism2+".ffn -db "+self.fileprefix+"/"+organism1+".db -outfmt 6 > "+self.fileprefix+"/"+organism2+"_"+organism1+".txt")
               print("RECIPROCAL BLAST...")
               os.system("python "+self.fileprefix+"/../reciprocal\ blast.py "+self.fileprefix+"/"+organism2+"_"+organism1+".txt "+self.fileprefix+"/"+organism1+"_"+organism2+".txt "+self.fileprefix+"/"+organism1+"_"+organism2+".out")
               print("SCREEN...")
               os.system("python "+self.fileprefix+"/../screen_both.py "+outputfile+" "+self.fileprefix+"/"+organism2+".ffn "+self.fileprefix+"/"+organism1+"_"+organism2+".out "+outputfile)
               print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
               print("RUNNING FIRST BLASTP...")
               os.system("blastp -query "+outputfile+" -db "+self.fileprefix+"/"+organism2+".db -outfmt 6 > "+self.fileprefix+"/"+organism1+"_"+organism2+".txt")
               print("RUNNING SECOND BLASTP...")
               os.system("blastp -query "+self.fileprefix+"/"+organism2+".faa -db "+self.fileprefix+"/"+organism1+".db -outfmt 6 > "+self.fileprefix+"/"+organism2+"_"+organism1+".txt")
               print("RECIPROCAL BLAST...")
               os.system("python "+self.fileprefix+"/../reciprocal\ blast.py "+self.fileprefix+"/"+organism2+"_"+organism1+".txt "+self.fileprefix+"/"+organism1+"_"+organism2+".txt "+self.fileprefix+"/"+organism1+"_"+organism2+".out")
               print("SCREEN...")
               os.system("python "+self.fileprefix+"/../screen_both.py "+outputfile+" "+self.fileprefix+"/"+organism2+".faa "+self.fileprefix+"/"+organism1+"_"+organism2+".out "+outputfile)
               print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print("****************************DONE****************************************")
      #blastp -query PA1.txt -db PA14.db -outfmt 6 > PA1_PA14
      #blastp -query PA14.txt -db PA1.db -outfmt 6 > PA14_PA1
      #python reciprocal\ blast.py PA14_PA1 PA1_PA14 rbb_out




