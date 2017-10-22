data={1:'a'}
print (data)

data[2]='b'
print (data)

data['name']='pey'
print (data)

data[3]=[1,2,3]
print (data)

del data[1]
print (data)

d={'name':'pey', 'phone':'01199993323','birth':'1118'}
#print (d.keys())
for k in d.keys():
    print (k)

print (list(d.keys()))
print (list(d.values()))
print (d.items())
#d.clear()
#print (d)
print (d.get('name'))

s1=set([1,2,3])
print (s1)

s1=set([1,2,3,4,5,6])
s2=set([9,7,8,6,5,4])

print (s1.difference(s2))
print (s2.difference(s1))

s3=list(s1)

print (s3.pop())

while s3:
    print( s3.pop())

print( "----")

import sys
a = 3
print( sys.getrefcount(3) )
b = 3
print( sys.getrefcount(3) )

a,b=('python','life')
print (a,b)

pin="881120-1068234"
ipos = pin.find('-')
print (pin[:ipos])
print (pin[ipos+1:])
print (pin[7])

a=[1,3,5,4,2]
a.sort( reverse=True)
#a.reverse()
print (a)

a=['Life','is','too','short']
c='life'
b=" "
#result=a[0]+a[1]+a[2]+a[3]
result=b.join(a)
print (result)

a=(1,2,3)
a=a+(4,)
print (a)

a={'A':90,'B':80,'C':70}
result=a.pop('B')
print (a)
print (result)

a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print (b)

a=b=[1,2,3]
a[1]=4
print (b)
