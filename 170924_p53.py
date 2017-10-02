# 'Pithon'이라는 문자열을 "Python"으로 바꿔보자.
# 문자열의 요소값은 바꿀 수가 없다.
# 문자열과 튜플은 immutable한 자료형이라고 한다.


strInput = "Pithon"
iGetPos = 0
for cTmp in strInput:
    if( cTmp == 'i'):
        break
    iGetPos += 1

strOutput = strInput[0:iGetPos] + 'y' + strInput[iGetPos+1:]
print(strOutput)
