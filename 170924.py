# 20170924
# @Jun.Soyoung
# local 변수와 global 변수의 사용원리는 c언어와 동일하다.
# 문자열에는 캐릭터하나 하나를 따로 가리길 수 있는 배열을 적용할 수 있다.
# 문자열에서 문자를 찾아낼 수 있다. 이것을 인덱싱이라고 한다.
# 문자열에서 문자열을 뽑아내는 방법을 슬라이싱이라고 한다.
#
#
'''
a = 10

def test():
    print(a)
    b = 20
    print(b)

test()


iData = 6
iData1 = 5
iRet = iData ** iData1
print( iRet )

iRet = 4 * 4 * 4 * 4 * 4
print ( iRet )

iRet = iData // iData1
print ( iRet )


iRet = iData / iData1
print ( iRet )

strData = "I'm a Soyoung. I'm going to study Japaness."
print( '"' + strData[15:]+ '"')

strData = "ABC"
strData1 = "YXZ"
strRet = strData * 3
print( strRet )

print( strData[0])
'''
# 문자열 포메팅
# %와 숫자를 결합할 때 스페이스를 추가해야 한다. 즉, '%' + ' ' + '3'
# 한 문장에 두개이상의 문자열 포멧 코드를 사용할 때는 ()로 묶어준다.
# 문자열 포멧코드 %s의 경우 숫자, 문자열, 실수 타입모두 허용가능하다.
#
# 문자열 포멧코드는 format()함수로 대체하여 사용할 수 있다.
'''
strData = "I eat %s apples." % '5'
print(strData)
strData = "I eat %s apples." % 3
print(strData)

iGet1 = 4
iGet2 = 7
strData = "I ate %s apples. so I was sick for %d days." % (iGet1, iGet2)
print(strData)
strData = "I ate {0} apples. so I was sick for {1} days.".format(iGet1, iGet2)
print(strData)

strData = "I ate {iGet1} apples. so I was sick for {iGet2} days.".format(iGet1=6, iGet2=9)
print(strData)
'''

'''
# 문자열 포멧코드의 정렬. 우측 정렬(%20s)과 좌측 정렬 ( %-20s)
strData = "Error is '%-10.3f%%'." % 89.897678
print(strData)

# 문자열 관련 함수들
# 문자의 수량 알려주기
iCount = strData.count("'")
print(iCount)
# 문자의 위치 알려주기
iPos = strData.find("a")  # return 값 있음.
print( "1. Position = %d " % iPos)
#iPos = strData.index("a") # 값이 존재하지 않으면 런타임 에러발생함.
#print( "2. Position = %d" % iPos)

# 문자열 삽입
# join 함수는 리턴으로 받아서 프린트해야 한다.
strSubValue = "..."
strOutput = strSubValue.join( strData )
print( strOutput )

# 문자열 바꾸기
strOutput = strData.replace("Error", "Pass")
print(strData + '  -->  ' + strOutput)

# 문자열 나누기 ( split() )
strOutput = strData.split('%')
print(strOutput)
'''
# 문자열 정렬
strData = ".." + "{0:=<10}".format("ABCD") + "..."
print(strData)

strData = ".." + "{0:*>10}".format("ABCD") + "..."
print(strData)

strData = ".." + "{0:$^10}".format("ABCD") + "..."
print(strData)

