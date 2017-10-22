# 정규식
'''
import re
Data = '92834098_23_293890'
result = re.findall('_(\d+)_', Data)
Datas = Data.split('_')

print( result )
print( Datas[1])
p = re.compile('[a-z]+')

m = p.search("python")
print( m)

if m:
    print( 'search found:', m.group())
else:
    print( 'no search')

result = p.findall('life is too short')
print( result)

result = p.finditer('life is too short')

print( result)
for r in result:
    print(r)

print( m.group())
print( m.start())
print( m.end())
print( m.span())
'''

# 제어문
