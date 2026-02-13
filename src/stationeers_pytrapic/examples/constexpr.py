from stationeers_pytrapic.symbols import *


@constexpr
def filter_by_sorting_class(cls, negate=False):
    condop = ConditionOperation.Equals
    if negate:
        condop = ConditionOperation.NotEquals
    condop = condop << 8
    cls = cls << 16
    return cls + condop + SorterInstruction.FilterSortingClassCompare


@constexpr
def filter_by_name(name, negate=False):
    hash = HASH(name) << 8
    instruction = SorterInstruction.FilterPrefabHashEquals
    if negate:
        instruction = SorterInstruction.FilterPrefabHashNotEquals
    return hash + instruction


# access the stack of a sorter
ores_sorter_stack = Stack(d0)
ores_sorter_stack[0] = filter_by_sorting_class(SortingClass.Ores)

no_ices_sorter_stack = Stack(d1)
no_ices_sorter_stack[0] = filter_by_sorting_class(SortingClass.Ices, negate=True)

# you can also get the stack by the reference id
only_steel = Stack(ref_id=0x3455)
only_steel[0] = filter_by_name("ItemSteelIngot")
