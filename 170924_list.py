# @Jun.Syoung
# list는 문자열과 마찬가지로 인덱싱과 슬라이싱이 가능하다.
# sort를 하려면 같은 데이터 타입이 있어야 한다.
a = ['2','1','3','4',[['c','b','a'],["life","is","wonderful"]]]
print(a[-1][-1][-1])

print(a)
print(a[1])

del a[4:]
print(a)

a.append( '5' )
print(a)

print('\n>> sort ...............')
a.sort()
print(a)

a.reverse()
print(a)

b = '3'
print('>> Position of %s is %s.' % (b, a.index(b)) )

a.insert(0, '0')
print(a)

a.remove( '5' )
print(a)

print(">> Posision to delete is %d. The value is '%s'. The result is %s." % ( 4, a.pop(4), a))

a = [2,4,2,5]
print(a)
a.extend( [6,3,7] )
print(a)

