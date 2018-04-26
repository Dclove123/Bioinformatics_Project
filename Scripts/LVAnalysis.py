def main ():
  #r = read, w = write, a = append
  #f = open("input.txt", "r"); read input.txt

  txt = open("/Bioinformatics_Project/Scripts/Data/DatabaseNewLRegionAA.txt", "r") #Parsed sequence of L regions
  txt = open("/Bioinformatics_Project/Scripts/Output/LVViterbiOutput.txt", "r") #ViterbiOutput file to be analyzed
  output = open("/Bioinformatics_Project/Scripts/Output/LVSeqOutAnalysis", "w")

  index = 1
  pairs = {}
  frequencies = {}
  total = 0
  last = ""