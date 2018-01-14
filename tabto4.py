import sys

src = sys.argv[1]
dsc = sys.argv[2]

print(src)
print(dsc)

f = open(src)
rText = f.read()
f.close()
rText_Rev = rText.replace("\t", " "*2)
print( rText + "\n.....\n" )

f_out = open(dsc, 'w')
f_out.write(rText_Rev)
f_out.close()
print( rText_Rev)
