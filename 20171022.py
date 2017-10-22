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
'''
caffe = 10
money = 300
while money:
    print( 'I will give coffee as your money')
    caffe -= 1
    print( 'The remained coffee is %d.'%caffe)
    if not caffe:
        print( 'The coffee is over.')
        break
'''

a = 0
while a<10:
    a += 1
    if a%2 == 0: continue
    print( a) # even print


# for문과 range 사용하기 : 1부터 10까지 더하기
sum = 0
for i in range(11):
    sum += i

print( sum)

# marks3.py
marks = [90,25,67,45,80]
for no in range( len(marks)):
    if( marks[no] < 60 ): continue
    print( '%d PASS!!' % marks[no])


# multiplication tables, not use \n in end of line
for i in range(2, 10):
    for j in range( 1, 10):
        print( '%2d x %2d = %2d' % ( i,j,i*j), end=" ")
    print( '')

# 리스트안에 for문 포함하기
a = [1,2,3,4,5,6]
result = [ (i*3) for i in a if i%2==0]
print( result)

# 연습문제
i = 0
while True:
    i += 1
    if i == 6: break;
    print( '*'*i)

A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for i in A:
    total = total + i

avg = total / len(A)
print( avg )





