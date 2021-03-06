def main():
    frequencyFileC = "/Bioinformatics_Project/Scripts/Output/DatabaseCOut.txt"
    frequencyFileV = "/Bioinformatics_Project/Scripts/Output/DatabaseVOut.txt"
    frequencyFileL = "/Bioinformatics_Project/Scripts/Output/DatabaseLOut.txt"
    
    testingDataLV = "/Bioinformatics_Project/Scripts/Output/LVSeqOut.txt"
    inputLV = open(testingDataLV,"r")
    fileC = open(frequencyFileC, "r")
    fileV = open(frequencyFileV, "r")
    fileL = open(frequencyFileL, "r")
    result = open("/Bioinformatics_Project/Scripts/Output/LVFixedViterbiOutput.txt", "w")

    resultTuple = ("",10.0e256)

    
    ##stateChangeFreq = {"CC": 0.99057, "CV": .00943, "VC": .010638, "VV": 0.98936}
    stateChangeFreq = {"LL": 0.9333333, "LV": 0.06666667, "VL": 0, "VV": 1}
    
    aminoAcidDict = {"A":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"K":0,"L":0,"M":0,"N":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"V":0,"W":0,"Y":0}
    print(aminoAcidDict)
    
    aaFreqC = fillDict(aminoAcidDict.copy(),fileC.readline())
    print(aaFreqC)
    aaFreqL =fillDict(aminoAcidDict.copy(),fileL.readline())
    print(aaFreqL)
    aaFreqV = fillDict(aminoAcidDict.copy(),fileV.readline())
    print(aaFreqV)
    
    for line in inputLV:
        if line[0] == ">" or line[0] == "\n":
            print(line)
            result.write(line)
        else:
            print(line)
            result.write(line)
            line = line.rstrip("\n")
            line = line.replace("*","")
            resultTuple = Viterbi(line,aaFreqL,aaFreqV,stateChangeFreq,resultTuple,True)
            print(resultTuple[0] , " " , resultTuple[1])
            result.write(resultTuple[0] + "\n")
            resultTuple = ("",10.0e256)
    
    test = fileC.readline()
    print(test)

def Viterbii(sequence,dictC,dictV,dictState,result,isV):     #Returns highest valued frequency
    #print(sequence)
    """if result[1] == 0:
        #print("FLOAT OVERFLOW")
        return result"""
    if sequence == "":
        result = list(result)
        if isV:
            result[0] = result[0] + "V"   
        else:
            result[0] = result[0] + "C"
        result = tuple(result)
        return result
    if result[0] == "":     #Make a beginning state here
        tempOne = (result[0],result[1])
        tempTwo = (result[0],result[1])
    elif result[0][-1] == "V":
        tempOne = (result[0],ViterbiCalc(sequence,dictV,dictState["VV"],result[1]))
        tempTwo = (result[0],ViterbiCalc(sequence,dictC,dictState["VC"],result[1]))
    elif result[0][-1] == "C":
        #print("V'd")
        tempOne = (result[0],ViterbiCalc(sequence,dictC,dictState["CC"],result[1]))
        tempOne = list(tempOne)
        tempOne[0] = tempOne[0] + "C"
        tempOne = tuple(tempOne)
        finalResultC = Viterbi(sequence[1:],dictC,dictV,dictState,tempOne,False)
        #print(finalResultC)
        return finalResultC
    if isV:
        tempOne = list(tempOne)
        tempOne[0] = tempOne[0] + "V"
        tempOne = tuple(tempOne)
        if result[0] == "":
            tempTwo = list(tempTwo)
            tempTwo[0] = tempTwo[0] + "V"
            tempTwo = tuple(tempTwo)
        else:
            tempTwo = list(tempTwo)
            tempTwo[0] = tempTwo[0] + "C"
            tempTwo = tuple(tempTwo)

    
    finalResultV = Viterbi(sequence[1:],dictC,dictV,dictState,tempOne,True)
    finalResultC = Viterbi(sequence[1:],dictC,dictV,dictState,tempTwo,False)



    if finalResultV[1] > finalResultC[1]:
        #print(finalResultC)
        return finalResultV
    else:
        #print(finalResultV)
        return finalResultC

    return result



    """if result[1] == 0:
        return result
    if sequence == "":
        return result
    if result[0] == "":     #Make a beginning state here
        tempOne = (result[0],result[1])
        tempTwo = (result[0],result[1])
    elif result[0][-1] == "C":
        tempOne = (result[0],ViterbiCalc(sequence,dictC,dictState["CC"],result[1]))
        tempTwo = (result[0],ViterbiCalc(sequence,dictV,dictState["CV"],result[1]))
    elif result[0][-1] == "V":
        #print("V'd")
        tempOne = (result[0],ViterbiCalc(sequence,dictV,dictState["VV"],result[1]))
        tempOne = list(tempOne)
        tempOne[0] = tempOne[0] + "V"
        tempOne = tuple(tempOne)
        finalResultV = Viterbi(sequence[1:],dictC,dictV,dictState,tempOne,False)
        #print(finalResultV)
        return finalResultV
        #tempTwo = (result[0],ViterbiCalc(sequence,dictC,dictState["VC"],result[1]))
    if isC:
        tempOne = list(tempOne)
        tempOne[0] = tempOne[0] + "C"
        tempOne = tuple(tempOne)
        if result[0] == "":
            tempTwo = list(tempTwo)
            tempTwo[0] = tempTwo[0] + "C"
            tempTwo = tuple(tempTwo)
        else:
            tempTwo = list(tempTwo)
            tempTwo[0] = tempTwo[0] + "V"
            tempTwo = tuple(tempTwo)

    
    finalResultC = Viterbi(sequence[1:],dictC,dictV,dictState,tempOne,True)
    finalResultV = Viterbi(sequence[1:],dictC,dictV,dictState,tempTwo,False)



    if finalResultC[1] > finalResultV[1]:
        #print(finalResultC)
        return finalResultC
    else:
        #print(finalResultV)
        return finalResultV

    return result"""

def Viterbi(sequence,dictL,dictV,dictState,result,isL):
    if result[1] == 0:
        return result
    if sequence == "":
        result = list(result)
        if isL:
            result[0] = result[0] + "L"   
        else:
            result[0] = result[0] + "V"
        result = tuple(result)
        return result
    if result[0] == "":     #Make a beginning state here
        tempOne = (result[0],result[1])
        tempTwo = (result[0],result[1])
    elif result[0][-1] == "L":
        tempOne = (result[0],ViterbiCalc(sequence,dictL,dictState["LL"],result[1]))
        tempTwo = (result[0],ViterbiCalc(sequence,dictV,dictState["LV"],result[1]))
    elif result[0][-1] == "V":
        #print("V'd")
        tempOne = (result[0],ViterbiCalc(sequence,dictV,dictState["VV"],result[1]))
        tempOne = list(tempOne)
        tempOne[0] = tempOne[0] + "V"
        tempOne = tuple(tempOne)
        finalResultV = Viterbi(sequence[1:],dictL,dictV,dictState,tempOne,False)
        #print(finalResultV)
        return finalResultV
        #tempTwo = (result[0],ViterbiCalc(sequence,dictL,dictState["VC"],result[1]))
    if isL:
        tempOne = list(tempOne)
        tempOne[0] = tempOne[0] + "L"
        tempOne = tuple(tempOne)
        if result[0] == "":
            tempTwo = list(tempTwo)
            tempTwo[0] = tempTwo[0] + "L"
            tempTwo = tuple(tempTwo)
        else:
            tempTwo = list(tempTwo)
            tempTwo[0] = tempTwo[0] + "V"
            tempTwo = tuple(tempTwo)

    
    finalResultL = Viterbi(sequence[1:],dictL,dictV,dictState,tempOne,True)
    finalResultV = Viterbi(sequence[1:],dictL,dictV,dictState,tempTwo,False)



    if finalResultL[1] > finalResultV[1]:
        #print(finalResultL)
        return finalResultL
    else:
        #print(finalResultV)
        return finalResultV

    return result
        
def ViterbiCalc(sequence,dict,stateMult,probability):
    try:
        temp = probability * float(dict[sequence[0]]) * float(stateMult)
        return temp
    except:
        return probability
    """temp = probability * float(dict[sequence[0]]) * float(stateMult)
    #print(temp)
    return temp"""

def fillDict(dictionary, data):
    temp = data.split("\t")
    x = 0
    for key in dictionary:
        dictionary[key] = temp[x]
        x+=1
    return dictionary
        

main()
