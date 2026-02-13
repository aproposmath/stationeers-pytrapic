from stationeers_pytrapic.symbols import *

# "stack" variable gives access to the IC10 stack directly
stack[0] = 123
db.Settings = stack[2] + stack[3]

# create stack variables for other devices (dX or by RefId)
stack_d3 = Stack(d3)
stack_d3[0] = 456

stack_dev = Stack(ref_id=0x2355)
stack_dev[0] = 789
