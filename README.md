# Stationeers PyTrapIC - Transpiler from Python to IC10

## What is PyTrapIC

PyTrapIC is a Python tool to convert simple python code into Stationeers IC10. Note that this code is **very limited** and **very experimental** (meaning: There will be bugs!). See below for features and limitations.

Some code examples are [below](#examples).

## How to use

[Online (recommended)](https://aproposmath.github.io/stationeers-pytrapic)

Offline

```
pip install git+https://github.com/aproposmath/stationeers-pytrapic.git
python -m stationeers-pytrapic some_simple_code.py
```

The output is written to stdout.

## Implementation status

**Features**

- autocomplete for all structure names and logic types (e.g. `WallLight["Some Name"].On.Maximum`) (limitation: currently any structure suggests any logic type)
- variable assignments
- arithmetic operations (`+`, `-`, `*`, `/`)
- if-else statements
- while loops
- intrinsics (all IC10 instructions can be called as functions with either variables / constants as arguments)
- optimization for constant expressions (e.g. `1 + 2` becomes `3`)
- read/write acessing individual structures (`d0.Activate = True`)
- read/write acessing structures by type (`AutoLathe.Activate = True`)
- read/write acessing structures by name (`my_value = WallLight["Some Name"].On.Maximum`)
- simple functions (no arguments, no return values)
- no automatic `push ra/pop ra` on nested function calls ([see this example](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/nested_function_calls.py))
- `global` statement (useful to mimic function return values)
- remove unused functions ([you can have one code file for ICs!](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/one_file_rules_them_all.py))
- remove unused labels

**NOT working**

- call functions from another function (use manual `push ra/pop ra` for now)
- function arguments / return values (use `global` variables)

**Planned Features**

- use `define` for constant expressions instead of `move`
- function inlining (if a function is only called once, it will be inlined into the caller)
- remove all labels (use relative jumps instead)
- boolean operations (`and`, `or`, `not`)
- function arguments
- break and continue statements
- lambda functions
- better type annotations for logic types (e.g. autocomplete shouldn't suggest `WallLight.RatioHydrogen`)
  -> Any source for structured data with all available types would be helpful
- more optimizations (constant expressions, dead code elimination, etc.)
- better register allocation (respect not only function scope but also variable scope)
- [you tell me!](https://github.com/aproposmath/stationeers-pytrapic/issues/new)

**NOT planned**

- anything that is not supported by IC10 (e.g. classes, exceptions, etc.)
- anything provided by the Python standard library (e.g. `math`, `random`, etc.)
- list, dict, set, tuple (maybe for constant expressions)
- comprehensions (maybe for constant expressions)

## How does it work

The transpiler itself is written in Python and uses [astroid](https://pypi.org/project/astroid/) to parse python code.

The web application uses [Pyodide](https://pyodide.org/) to run the transpiler in the browser. The editor is based on [monaco](https://microsoft.github.io/monaco-editor/) and uses [monaco-pyright-lsp](https://github.com/SardineFish/monaco-pyright-lsp) for code completion. No data is sent to the server, everything is running in the browser.

## Examples

- [Airlock](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/airlock.py)
- [Solar tracking](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/solar.py)
- [Nested function calls](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/solar.py)
- [Have code for multiple ICs in one File](https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/examples/one_file_rules_them_all.py)

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

GlassDoor[h_in].Lock = True
GlassDoor[h_out].Lock = True
ActiveVent[h_in].Mode = True
ActiveVent[h_in].On = False
ActiveVent[h_out].Mode = True
ActiveVent[h_out].On = False

while True:
    if DiodeSlide[h_switch].On.Maximum > 0:
        going_out = GlassDoor[h_in].Open.Maximum > 0
        dir_to = h_out if going_out else h_in
        dir_from = h_in if going_out else h_out
        GlassDoor[dir_from].Open = False
        ActiveVent[dir_from].On = True

        while GasSensor.Pressure.Maximum != 0:
            pass
        sleep(0.2)

        ActiveVent[dir_from].On = False
        GlassDoor[dir_to].Open = True
        DiodeSlide[h_switch].On = False
        sleep(1)
```

</td>
<td>

```asm
move r0 HASH("In")
move r1 HASH("Out")
move r2 HASH("Switch")
sbn -324331872 r0 Lock 1
sbn -324331872 r1 Lock 1
sbn -1129453144 r0 Mode 1
sbn -1129453144 r0 On 0
sbn -1129453144 r1 Mode 1
sbn -1129453144 r1 On 0
lbwhile1:
  lbn r3 576516101 r2 On 3
  ble r3 0 lbelse2
    lbn r5 -324331872 r0 Open 3
    sgt r4 r5 0
    select r6 r4 r1 r0
    select r7 r4 r0 r1
    sbn -324331872 r7 Open 0
    sbn -1129453144 r7 On 1
lbwhile9:
    lb r8 -1252983604 Pressure 3
    beq r8 0 lbwhile.end9
      j lbwhile9
lbwhile.end9:
    sleep 0.2
    sbn -1129453144 r7 On 0
    sbn -324331872 r6 Open 1
    sbn 576516101 r2 On 0
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

panels = SolarPanel  # port facing north
sensor = d1  # port facing east

while True:
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical
```

</td>
<td>

```asm
lbwhile1:
  l r0 d1 Horizontal
  sb -2045627372 Horizontal r0
  l r1 d1 Vertical
  sub r2 90 r1
  sb -2045627372 Vertical r2
  j lbwhile1
```

</td>
</tr>
</table>
