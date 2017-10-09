# Q1. 주민번호 나누기

Pin = "881120-1068234"
iCount = 0
for cTmp in Pin:
    if( cTmp == '-'):
        break
    iCount = iCount + 1

print( Pin[:iCount])
print( Pin[iCount+1:])

# Q2. 성별을 표시하기

print( Pin[iCount+1:iCount+2])

# Q3. 리스스 정렬
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# Q4. 리스트를 문자열로 만들기
a=['Life','is','too','short']
result = a[0] + " " + a[1] + " " + a[2] + " " + a[3]
b = " ".join(a)
print( result)
print( b)


