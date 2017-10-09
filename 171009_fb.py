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