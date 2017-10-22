# 1. from FB
# expect value = 0^0, 1^2, 2^2, 3^2, 4^2
# 2. dictionary example

print( '-'*50)
iInput = [ x**2 for x in range(0,5)]
print( iInput)

lGrade={'pey':10, 'julliet':90, 'abc':70}
print( lGrade['pey'])
print( lGrade.keys())

print( '-'*50)
for k in lGrade.keys():
    print(k)

print( list( lGrade.keys())) # make list

print( list(lGrade.values())) # make list. If you delete list(), will be printed "dict_value([...])

print( lGrade.items())
print( list(lGrade.items()))
print( lGrade.get('abcdse', 'none_key')) # key가 없으면 두번째 아규먼트인 디폴트값을 반환한다.
print( 'abcd' in lGrade)
print( 'pey' in lGrade)
print( '-'*50)

# 집합 자료형 : 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9,10])
print( s1 & s2) # 교집합
print( s1.intersection( s2))
print( s1 | s2) # 합집합
print( s1.union(s2))
print( s1 - s2) # 차집합
print( s2 - s1)
print( s1.difference(s2))
print( s2.difference(s1))
s1.add( 20)
print( s1)
s1.update( [12,13,14])
print(s1)
print( '-'*50)
# 자료형의 참과 거짓
while s1:
    print( s1.pop()) # 마지막 데이터부터 가져와야 하는데 앞쪽 데이터를 가져왔다. ??? 확인할 것. ??? --> list가 아니다. 집합이다. 순서가없다.

print( '-'*50)
lData = [1,2,3,4,5]
while lData:
    print( lData.pop()) # pop은 마지막 데이터부터 가져온다.

print( '-'*50)

print( type(4))

import sys
a = 3
print( sys.getrefcount(3))  # 3이라는 정수형 객체에 참조개수를 반환한다.
b = 3
print( a is b)

print( sys.getrefcount(3))
del(a)
del(b)
print( sys.getrefcount(3))


print( '-'*50)
from copy import copy
a = [1,2,3]
b = a
c = a[:]
d = copy( a)
a[0] = 9
print( a)
print( b)
print( c)
print( d)

print( '-'*50)

