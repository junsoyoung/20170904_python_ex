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

'''
# 함수 사용하기
'''
def say():
    print( 'hi')

def sum_many(*args):
    sum = 0;
    for i in args:
        sum += i
    return sum

def sum_mul( choice, *args):
    if choice == 'sum':
        result = 0;
        for i in args:
            result += i
    elif choice == "mul":
        result = 1;
        for i in args:
            result *= i

    return result

def vartest(a):
    a += 1
    return a
'''
'''
say()
result = sum_many(1,2,3,4,5,40)
print(result)

result = sum_mul( 'sum', 2,2,4,1,2,3)
print( result)
result = sum_mul( 'mul', 2,2,4,1,2,3)
print( result)

a = 1
print( vartest(a))
print( a)
'''
# 입출력
'''
no = input( 'please, input no  ')
print( no)
'''
"""
x = 3
y = 2
print(x>y)


a="Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

i=0
while True:
    i+=1
    if i>5: break
    print("*"*i)

a=[70,60,55,75,95,90,80,80,85,100]

total=0
for val in a:
    total+=val
average=total/len(a)
print(average)

def sum_mul(choice,*args):
    if choice=="sum":
        result=0
        for i in args:
            result=result+i
    elif choice=="mul":
        result=1
        for i in args:
            result=result*i
    return result

result=sum_mul('sum',1,2,3,4,5)
print (result)

result=sum_mul('mul',1,2,3,4,5)
print(result)
"""

#f=open("new.txt",'w')
#for i in range(1,11):
#    data="%d번째 줄입니다.\n" %i
#    f.write(data)
#f.close()


import sys
args = sys.argv[1:]

f=open( args[0],'r')
f1 = open(args[1],'w')

while True:
    line=f.readline()
    if "AAA" in line and "BBB" in line:
        f1.write(line)
        print(line)
    if not line:break
    print(line)
f.close()
f1.close()


'''
f=open("sample.txt")
lines=f.readlines()
f.close()

total=0
for line in lines:
    score=int(line)
    #print(line)
    total+=score
average=total/len(lines)
f=open("result.txt",'w')
f.write("%f" % average)
f.close()
'''