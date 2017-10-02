# 2017.9.7 @Soyoung jun

'''
value = 12
r = range(3, value)
for k in r:
    m=k%2
    if m==0:
        print(k, "짝수")
    else:
        print(k, "odd")
'''
'''
import sys

print( "num of arg:",len(sys.argv), 'args')
print("arg list:", str(sys.argv))

### 아규먼트사용법 찾아볼것

form	=	"""	My	name	is	{name}	"""
print(form.format(name='Sonic'))
'''
print("<START> ", "-"*50)
'''
strGet1 = input(" GetData1 = ")
strGet2 = input(" GetData2 = ")
print( strGet1, " + ", strGet2, " = ", int(strGet1) + int(strGet2))


x = {'name':'syoung', 'age':44, 'address':'sechun'}
dir(x)
for mydata in x:
    print(mydata, x[mydata])
    '''

#print( "%10s" % "hi")
#print( "%-10sABCD" % "hi")

#print( "%0.4f" % 3.413480938498)
#print( "%10.4f" % 3.41348093)
#print( "%-10.4f" % 3.41348093)

#strData = "Life is too sh:ort"
#print( strData.split(":"))

strData = "{0:@<10}".format("hi")
print( strData)


strData = "{0:!>20}".format("hi")
print( strData)

strData = "{0:^20}".format(4.345)
print( strData)
print( type(strData))


print("<__END> ", "-"*30)






