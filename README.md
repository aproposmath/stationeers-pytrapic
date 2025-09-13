# Stationeers PyTrapIC - Transpiler from Python to IC10

## What is PyTrapIC

PyTrapIC is a Python tool to convert simple python code into Stationeers IC10. Note that this code is **very limited** and **very experimental** (meaning: There will be bugs!). See below for features and limitations.

Some code examples are [below](#examples).

## How to use

- [Stationeers Mod](mod/README.md)

- [Online Editor](https://aproposmath.github.io/stationeers-pytrapic)

- Command line tool

```
pip install git+https://github.com/aproposmath/stationeers-pytrapic.git
python -m stationeers-pytrapic some_simple_code.py
```

The output is written to stdout.

## Implementation status

**Python Features**

- read/write acessing individual structures (`WallHeater(d0).Activate = True`)
- read/write acessing structures by type (`AutoLathes.Activate = True`)
- read/write acessing structures by name (`my_value = WallLights["Some Name"].On.Maximum`)
- Slot access, either by name (`furnace.Export.Occupied`) or by index (`furnace.slot0.Occupied`).
- intrinsics (all IC10 instructions can be called as functions, e.g. `a = pop()` or `x = lb(HASH("StructureWallHeater", "On", "Maximum")`)
- variable assignments
- arithmetic operations (`+`, `-`, `*`, `/`, `%`, `+=`, `-=`, `*=`, `/=`)
- boolean operations (`and`, `or`, `not`)
- unary operations (`not`, `-`)
- if-else statements
- while loops
- type hints/autocomplete for all structure names and logic types (e.g. `WallLights["Some Name"].On.Maximum`)
- optimization for constant expressions (e.g. `1 + 2` becomes `3`)
- functions
- `global` statement (useful to mimic function return values or store state between function calls)
- remove unused functions ([you can have one code file for all your ICs!](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/one_file_to_rule_them_all.py))
- remove all labels
- function inlining (if a function is only called once, it will be inlined into the caller)
- break and continue statements
- return statements ( no return values yet )
- function arguments (only simple values (float), no structures like `DaylightSensor(d0)` )
- function return values

**Planned Features**

- Access slot by variable index (`furnace.slots[i].Occupied`)
- push/pop `ra` automatically in nested function calls ([use manual `push ra/pop ra` for now)](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/nested_function_calls.py))
- better register allocation (check scope in ic10 code instead of python code for more granularity)
- pass function arguments/return values in registers (currently only via stack)
- allow structures as function arguments/return values (currently only simple values like `float` are allowed)
- for loops
- [you tell me!](https://github.com/aproposmath/stationeers-pytrapic/issues/new)

**NOT planned**

- lambda functions
- anything that is not supported by IC10 (e.g. classes, exceptions, etc.)
- anything provided by the Python standard library (e.g. `math`, `random`, etc.)
- list, dict, set, tuple, comprehensions (maybe later, but only for constant expressions)

## How does it work

The transpiler itself is written in Python and uses [astroid](https://pypi.org/project/astroid/) to parse python code.

The web application uses [Pyodide](https://pyodide.org/) to run the transpiler in the browser. The editor is based on [monaco](https://microsoft.github.io/monaco-editor/) and uses [monaco-pyright-lsp](https://github.com/SardineFish/monaco-pyright-lsp) for code completion. No data is sent to the server, everything is running in the browser.

## Examples

- [Airlock](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/airlock.py)
- [Solar tracking](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/solar.py)
- [Nested function calls](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/nested_function_calls.py)
- [Have code for multiple ICs in one File](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/one_file_to_rule_them_all.py)

<table>
<th>Python</th>
<th>IC10</th>

<tr>
<td>

```py

from stationeers_pytrapic.symbols import *

# Airlock, see examples/airlock.py for mor info

h_in = HASH("In")
h_out = HASH("Out")
h_switch = HASH("Switch")

GlassDoors[h_in].Lock = True
GlassDoors[h_out].Lock = True
ActiveVents[h_in].Mode = True
ActiveVents[h_in].On = False
ActiveVents[h_out].Mode = True
ActiveVents[h_out].On = False

while True:
    if DiodeSlides[h_switch].On.Maximum > 0:
        going_out = GlassDoors[h_in].Open.Maximum > 0
        dir_to = h_out if going_out else h_in
        dir_from = h_in if going_out else h_out
        GlassDoors[dir_from].Open = False
        ActiveVents[dir_from].On = True

        while GasSensors.Pressure.Maximum != 0:
            pass
        sleep(0.2)

        ActiveVents[dir_from].On = False
        GlassDoors[dir_to].Open = True
        DiodeSlides[h_switch].On = False
        sleep(1)
```

</td>
<td>

```asm
sbn -324331872 HASH("In") Lock 1
sbn -324331872 HASH("Out") Lock 1
sbn -1129453144 HASH("In") Mode 1
sbn -1129453144 HASH("In") On 0
sbn -1129453144 HASH("Out") Mode 1
sbn -1129453144 HASH("Out") On 0
lbwhile1:
  lbn r3 576516101 HASH("Switch") On 3
  ble r3 0 lbelse2
    lbn r3 -324331872 HASH("In") Open 3
    sgt r0 r3 0
    select r1 r0 HASH("Out") HASH("In")
    select r2 r0 HASH("In") HASH("Out")
    sbn -324331872 r2 Open 0
    sbn -1129453144 r2 On 1
lbwhile8:
    lb r3 -1252983604 Pressure 3
    beq r3 0 lbwhile.end8
      j lbwhile8
lbwhile.end8:
    sleep 0.2
    sbn -1129453144 r2 On 0
    sbn -324331872 r1 Open 1
    sbn 576516101 HASH("Switch") On 0
    sleep 1
lbelse2:
  j lbwhile1
```

</td>
</tr>
<tr>
<td>

```py
from stationeers_pytrapic.symbols import *

panels = SolarPanels  # port facing north
sensor = DaylightSensor(d0)  # port facing east

while True:
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical
```

</td>
<td>

```asm
lbwhile1:
  l r0 d0 Horizontal
  sb -2045627372 Horizontal r0
  l r0 d0 Vertical
  sub r1 90 r0
  sb -2045627372 Vertical r1
  j lbwhile1
```

</td>
</tr>
</table>
