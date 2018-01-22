def comp_string( input_str):
    iCnt = 0
    szTmp = ""
    szResult = ""
    for cData in input_str:
        if cData != szTmp:
            if iCnt>0:
                szResult += str(iCnt)
            szResult += cData
            szTmp = cData
            iCnt = 1
        else:
            iCnt += 1

    if iCnt>0:
        szResult += str(iCnt)
    return szResult


rData1 = input("Input String :")
print(comp_string(rData1))

