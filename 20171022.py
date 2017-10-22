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
"""
prompt = '''
1.Add
2.Del
3.List
4.Quit

Enter No.'''
No = 0

while No !=4:
    print( prompt)
    No = int(input())
"""
# 커피자판기 이야기
caffe = 10
money = 300
while money:
    print( 'I will give coffee as your money')
    caffe -= 1
    print( 'The remained coffee is %d.'%caffe)
    if not caffe:
        print( 'The coffee is over.')
        break


