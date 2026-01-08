from stationeers_pytrapic.symbols import *

@constexpr
def _get_comp_number(comp):
    if comp == "equals":
        return 0
    elif comp == "greater":
        return 1
    elif comp == "less":
        return 2
    elif comp == "not_equals":
        return 3
    else:
        raise ValueError(f"Unknown comparison operator: {comp}")

@constexpr
def equals(name):
    return HASH(name) << 8 | 0x01

@constexpr
def not_equals(name):
    return HASH(name) << 8 | 0x02

@constexpr
def by_sorting_class(class_number, comp="equals"):
    comp = _get_comp_number(comp)
    return class_number << 16 | comp << 8 | 0x03

@constexpr
def by_slot_type(slot_number, comp="equals"):
    comp = _get_comp_number(comp)
    return slot_number << 16 | comp << 8 | 0x03

@constexpr
def by_quantity(n, comp="equals"):
    comp = _get_comp_number(comp)
    return n << 16 | comp << 8 | 0x03
