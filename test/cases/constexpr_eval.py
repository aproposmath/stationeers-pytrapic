from stationeers_pytrapic.symbols import *

@constexpr
def build_instruction(name, count):
    return HASH(name) << 16 | count << 8 | 0x02

def build_plastic_sheets():
    lathe_id = Autolathes.Minimum.ReferenceId
    lathe_stack = Stack(ref_id=lathe_id)
    lathe_stack[0] = build_instruction("ItemPlasticSheets", 10)

def build_cables():
    printer_id = ElectronicsPrinters.Minimum.ReferenceId
    printer_stack = Stack(ref_id=printer_id)
    printer_stack[printer_stack[63]+1] = build_instruction("ItemCableCoil", 50)


button_sheets = LogicButton(d1)
button_cables = LogicButton(d2)

while True:
    yield_()
    if button_sheets.Setting:
        build_plastic_sheets()
    if button_cables.Setting:
        build_cables()

