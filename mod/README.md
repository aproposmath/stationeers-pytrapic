# Stationeers PyTrapIC - Transpiler from Python to IC10

This mod allows you to write code for Stationeers' ICs in Python instead of IC10 assembly language. The Python code is converted into IC10 code when you `Export` it from the in-game editor.

## Installation

This mode requires [BepInEx](https://github.com/BepInEx/BepInEx).
Download the latest release from the [releases page](https://github.com/aproposmath/stationeers-pytrapic/releases) and unzip it into your `BepInEx/plugins` folder.

## Features

- Write code in Python instead of IC10 assembly language
- Supports a subset of Python (see [here](https://github.com/aproposmath/stationeers-pytrapic/blob/dev/README.md#implementation-status) for details)
- Use the in-game [libraries](#Libraries) feature to reuse commonly used functions across multiple ICs/save games
- Syntax highlighting
- Compile errors are shown as tooltip
- Intrinsics: all IC10 commands are available as Python function

## Usage Notes

- ICs are not running Python, your Python code is tranlated to IC10 code when you `Export` it from the in-game editor
- No new parts are added to the game, you do the programming with a Computer/Laptop and the IC Editor Motherboard
- To write Python code, the **first** line of your code must **exactly** match `from stationeers_pytrapic.symbols import *`, otherwise it is treated as IC10 code
- You can use the [online editor](https://aproposmath.github.io/stationeers-pytrapic/) to write and test your code before using it in-game (better autocompletion, syntax highlighting, error checking, etc.)
- IC10 code is still supported
- When you remove the mod, your ICs will still work as they are still running IC10 code, but the original Python code of the chip will be lost. (your libraries are still kept though)
- The last stack entries (511, 510, ...) are used for function arguments and return values, the stack pointer is not modified by the transpiler
- All structures have the same name as in the Stationpedia, but without the `Structure` suffix (e.g. `WallHeater`, `SolarPanels`, `DaylightSensor`, etc.)
- Use single structures by port (`WallHeater(d0)`) or multiple structures by type with suffix `s` (`WallHeaters`).
- Access structures by name using square brackets (`WallHeaters["Greenhouse"]`)

## Libraries
You can store commonly used functions in a `Library` and import them into your Python code using `import library.your_lib_name`.

```python
from stationeers_pytrapic.symbols import *

# This is your library code stored in a Library named "python_solar"

def align_solar_panels():
    panels = SolarPanels  # port facing north
    sensor = DaylightSensor(d0)  # port facing east
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical

```

```python
from stationeers_pytrapic.symbols import *

# import your library
import library.python_solar

while True:
    align_solar_panels()  # call the function from your library
```


## Known Limitations/Issues

- Compile errors in tooltip show wrong line numbers when using libraries.
- No slots access (only via intrinsics)

## Planned Features

- Support for more Python features [see here](https://github.com/aproposmath/stationeers-pytrapic)
- More compile options in-game (e.g. optimization level, function inlining, etc.)
- IC10 preview in-game
- Better Lua support (see below)
- Importing Lua libraries from Python and vice versa
- [you tell me!](https://github.com/aproposmath/stationeers-pytrapic/issues/new)

## Experimental Features

- Limited Lua support (the first code line must be `require("stationeers_pytrapic.symbols")`)

