def main():
  sequence = ""
  fileoutput = ""
  aminoacidstrand = ""

  txt = open("/Bioinformatics_Project/Data/LVSeqOut_pre.txt", "r")
  output = open("/Bioinformatics_Project/Scripts/Output/LVSeqOut.txt", "w")

  length = 0
  ratio = {}
  numberseqences=0


  for line in txt:
    #piece the aminoacid sequences together
    if line[0] == ">":
      output.write("\n")
      output.write(line)

    else:
      line = line.strip("\n\t")
      output.write(line)         

  #print (ans)
  #output.write(str(ans))

  output.close()
  txt.close()

main()