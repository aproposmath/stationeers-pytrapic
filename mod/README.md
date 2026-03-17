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

---

## Developer Setup

The mod is a C# BepInEx plugin built with the .NET SDK. The build system is MSBuild and lives mostly in the `Template/` git submodule at the project root.

### Prerequisites

- **.NET SDK 10** (see `global.json` at the repo root; `rollForward: latestMajor` means newer major versions also work)
- **Python 3** — required by the `GenerateVersion` MSBuild target that runs before every build
- **Stationeers** — needed to compile against the game's DLLs (see [Game DLLs](#game-dlls) below)

### Clone with submodule

The `Template/` directory is a git submodule. Initialise it after cloning:

```sh
# git
git submodule update --init

# jj (if using Jujutsu)
jj git submodule update --init
```

### Game DLLs

The build needs Stationeers' managed DLLs (e.g. `Assembly-CSharp.dll`). The build system tries to locate them automatically, then falls back to the checked-in stub libraries in `Template/libs/`.

**Auto-detection order** (from `Template/FindStationeers.props`):

| Priority | Condition |
|----------|-----------|
| 1 | `STATIONEERS_DIR` environment variable |
| 2 | Default Windows Steam paths (`C:/Program Files (x86)/Steam/…`, `D:/…`, `E:/…`) |
| 3 | Default Linux Steam paths (`~/.steam/steam/…`, `~/Steam/…`, `$STEAMROOT/…`) |
| 4 | `StationeersDirectory` set in `Local.Developer.props` |
| 5 | CI fallback: `Template/libs/` (used automatically when `GITHUB_ACTIONS=true`) |

**macOS**: Stationeers has no macOS client, so the game DLLs are never present. The build will automatically use the checked-in stub libraries in `Template/libs/`. No extra steps needed.

**Linux / Windows with non-standard Steam path**: create a `Local.Developer.props` file in the repo root (it is gitignored) to override the path:

```xml
<Project>
  <PropertyGroup>
    <StationeersDllDir>/path/to/Stationeers/rocketstation_Data/Managed</StationeersDllDir>
  </PropertyGroup>
</Project>
```

You can also set the `STATIONEERS_DIR` environment variable to the Stationeers install root (the directory containing `rocketstation_Data/`) instead.

### Download mod dependencies

The mod depends on two external DLLs (the IC10 editor and StationeersLaunchPad) that are not in the repo. Download them once from the project root:

```sh
python3 Template/download_dependencies.py
```

This reads the `<Dependencies>` URLs from `Main.props` and extracts the DLLs into `Template/dependencies/`.

### Building

From the **repo root** (where `Main.csproj` lives):

```sh
dotnet build -c Debug Main.csproj
```

Or use the convenience script from `mod/` (also installs into BepInEx plugins):

```sh
cd mod && ./build.sh
```

`build.sh` defaults the install path to `~/.sa/Stationeers/BepInEx/plugins/`. Override it with:

```sh
STATIONEERS_MOD_DIR=/your/path/BepInEx/plugins ./build.sh
```

### IDEs

Any editor with MSBuild/C# support works. Open `Main.csproj` (at the repo root) as the project file.

- **JetBrains Rider** — open `Main.csproj` directly; Rider picks up NuGet sources from `NuGet.Config` automatically
- **Visual Studio** (Windows) — open `Main.csproj`; restores NuGet packages on first build
- **VS Code** — install the [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) extension, then open the repo root folder

`Local.Developer.props` is the right place for any machine-specific overrides (Stationeers path, Python executable name, etc.) so they stay out of version control. An example file to override the Python executable on systems where it is `python3` instead of `python`:

```xml
<Project>
  <PropertyGroup>
    <PythonExec>python3</PythonExec>
  </PropertyGroup>
</Project>
```

### Building a release zip

From the repo root:

```sh
cd mod && ./release.sh
```

Output: `dist/PyTrapIC.zip`, ready to unzip into `BepInEx/plugins/`.

