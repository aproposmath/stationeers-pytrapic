# Stationeers PyTrapIC - Transpiler from Python to IC10

This mod allows you to write code for Stationeers' ICs in Python instead of IC10 assembly language. The Python code is converted into IC10 code when you `Export` it from the in-game editor.

## Installation

This mode requires [BepInEx](https://github.com/BepInEx/BepInEx).
Download the latest release from the [releases page](https://github.com/aproposmath/stationeers-pytrapic/releases) and unzip it into your `BepInEx/plugins` folder.

## Usage Notes

- No new parts are added to the game, you do the programming with a Computer/Laptop and the IC Editor Motherboard
- To write Python code, the first line of your code must **exactly** match `from stationeers_pytrapic.symbols import *`, otherwise it is treated as IC10 code
- Syntax highlighting is available
- Compile errors are shown in the tooltip
- You can use the [online editor](https://aproposmath.github.io/stationeers-pytrapic/) to write and test your code before using it in-game (better autocompletion, syntax highlighting, error checking, etc.)
- On clicking `Export` in the in-game editor, your Python code is transpiled to IC10 and written to the IC
- IC10 code is still supported
- When you remove the mod, your ICs will still work as they are still running IC10 code, but the original Python code of the chip will be lost. (your libraries are still kept though)

### Libraries
You can store common functions in a `Library` and import them into your Python code using `import library.your_lib_name`.

Known issue: The compile errors show wrong line numbers when using libraries. (This is because the library code is prepended to your code before compiling it)

## Planned Features

- Show code size (bytes and lines) and register usage in the editor
- Support for more Python features [see here](https://github.com/aproposmath/stationeers-pytrapic)
- [you tell me!](https://github.com/aproposmath/stationeers-pytrapic/issues/new)
