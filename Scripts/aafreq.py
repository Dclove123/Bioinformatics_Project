def aminoacidfrequency(name, sequence, output):
  #only count the 20 amino acids
  aminoacid = {"A":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "K":0, "L":0, "M":0, "N":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "V":0, "W":0, "Y":0}
  length = 0
  index = 0
  ratio = {}
  ans = ""

  #count number of times each amino acid shows
  while index < len(sequence):
    length += 1
    letter = str(sequence[index])
    if letter in aminoacid:
      aminoacid[letter] += 1
    index += 1
  name = name.strip("\n")
  ans = "\n" + name + "\t"
  print ()

  # calculate ratios of each amino acid
  for n in aminoacid.keys():
    freq = aminoacid[n] / length
    number = aminoacid[n]
    ratio[n] = round(freq,5)

  # amino acids in alpha order  
  for i in sorted(ratio):
    ans = ans + str(ratio[i]) + "\t"

  print (ans)
  output.write(str(ans))




def main():
  sequence = ""
  fileoutput = ""
  aminoacidstrand = ""

  txt = open("/Bioinformatics_Project/Data/DatabaseCRegionAA.txt", "r")
  output = open("/Bioinformatics_Project/Scripts/Output/DatabaseCOut.txt", "w")

  #lineone = "PROTEIN" + "\t" + "A" + "\t" + "C" + "\t" + "D" + "\t" + "E" + "\t" + "F" + "\t" + "G" + "\t" + "H" + "\t" + "I" + "\t" +"K" +"\t"+ "L"+"\t"+ "M"+"\t"+ "N"+"\t"+"P" +"\t"+ "Q" +"\t"+ "R"+"\t"+ "S" +"\t"+ "T" +"\t"+ "V"+"\t"+ "W" +"\t"+ "Y"
  #output.write(lineone)
  previousname = txt.readline()

  for line in txt:
    #piece the aminoacid sequences together
    if line[0] != ">":
      aminoacidstrand += line.strip("\n\t")

    elif line[0] == ">":
      newname = line
      fileoutput = fileoutput + 2*"\n" + previousname + aminoacidstrand
      aminoacidfrequency(previousname, aminoacidstrand, output)

      #reset for next protein
      aminoacidstrand = ""
      previousname = newname
    #input()
  output.close()
  txt.close()

main()