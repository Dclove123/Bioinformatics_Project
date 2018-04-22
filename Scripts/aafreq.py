def main():
  sequence = ""
  fileoutput = ""
  aminoacidstrand = ""

  txt = open("/Bioinformatics_Project/Data/DatabaseVRegionAA.txt", "r")
  output = open("/Bioinformatics_Project/Scripts/Output/DatabaseVOut.txt", "w")

  dictionary = {"A":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "K":0, "L":0, "M":0, "N":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "V":0, "W":0, "Y":0}
  length = 0
  ratio = {}
  ans = ""
  numberseqences=0


  for line in txt:
    #piece the aminoacid sequences together
    if line[0] == ">":
      numberseqences+=1

    else:
      line = line.strip("\n\t")
      for char in line:
        if char in dictionary:
          dictionary[char] += 1
        length+=1

  for n in dictionary.keys():
    freq = dictionary[n] / length
    number = dictionary[n]
    ratio[n] = round(freq,5)

  # amino acids in alpha order  
  for i in sorted(ratio):
    ans = ans + str(ratio[i]) + "\t"

  ans += str(length) + "\t"
  ans += str(numberseqences)

  print (ans)
  output.write(str(ans))

  output.close()
  txt.close()

main()