result = 0
for n in range(1,1000):
    if( n%3 == 0 or n%5 ==0 ):
        result += n

print(result)

try:
    iMok = 4/0
    iNa  = 4%0
except ZeroDivisionError as e_msg:
    print(e_msg)

else:
    lData = [iMok, iNa]
    print( lData )

finally:
    print("---------------> end")

print(eval('1+3'))
print(eval("'hi ' + 'python'"))

print(hex(432)) # integer -> hex decimal

Sum_func = lambda a,b: a+b
print(Sum_func( 4, 5))
MyList_func = [lambda a,b:a+b, lambda a,b:a*b]
print(MyList_func)
print(MyList_func[0]( 4, 9 ))
print(MyList_func[1]( 4, 9 ))

print("----------------------------- map start")
'''
def two_times(x):
    return x*2
print(list( map( two_times, [1,2,3,4])))
'''
print(list( map( lambda x:x*2, [1,2,3,4])))
print("----------------------------- map __end")

