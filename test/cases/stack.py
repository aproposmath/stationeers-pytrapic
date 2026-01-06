from stationeers_pytrapic.symbols import *

stack[123] = 999.9
st = Stack()
a = 13 + stack[12]
st[a] = stack[9]

st0 = Stack(d4)
a = 13 + st0[a]
st0[a] = st0[9]

st1 = Stack(ref_id=0xFF)
a = 13 + st1[a]
st1[a] = st1[9]


a = stack[88]
stack[a] = a

a = db.Setting
stack[a+a] = 10*a
