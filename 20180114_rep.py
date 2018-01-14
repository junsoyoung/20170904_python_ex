import re

p_Re = re.compile('[a-z]+')

m_Re = p_Re.match("python")
if m_Re:
    print(m_Re)
    print( m_Re.group())
else:
    print("not match")

s_Re = p_Re.search("3 python")
if s_Re:
    print(s_Re)
    print(s_Re.group())
else:
    print("not search")


ret_Re = p_Re.findall("life is too short")
print(ret_Re)

ret_Re_itr = p_Re.finditer("life is too short")

for r in ret_Re_itr:
    print( r)
    print( r.group())
    print( r.start())
    print( r.end())
    print( r.span())

