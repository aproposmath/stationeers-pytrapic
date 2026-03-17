# PyTrapIC Webapp

Browser-based IDE for PyTrapIC. Write Python on the left, get IC10 assembly on the right — no server involved. The transpiler runs entirely in-browser via [Pyodide](https://pyodide.org/) (Python WASM), and the editor is [Monaco](https://microsoft.github.io/monaco-editor/) with Pyright-powered type checking via [monaco-pyright-lsp](https://github.com/SardineFish/monaco-pyright-lsp).

The production build is deployed to GitHub Pages at https://aproposmath.github.io/stationeers-pytrapic.

## Prerequisites

- **Node.js** (v18+) and **yarn**
- **Python 3.10+** with a working venv — needed only to generate the data files (see below)

See the [root README Developer section](../README.md#developer--contributor-setup) for Python environment setup.

## Setup

The `webapp/data/` directory is gitignored. It holds two generated files that must exist before you can run the dev server:

| File | Purpose |
|------|---------|
| `stationeers_pytrapic.zip` | Pyright type stubs (`.pyi` files), used by Monaco for autocompletion |
| `stationeers_pytrapic-0.0.1-py3-none-any.whl` | The transpiler Python wheel, fetched and unpacked by Pyodide at runtime |

Generate them from the repo root (with the venv active):

```sh
source .venv/bin/activate
./scripts/build_data.sh
```

Then install frontend dependencies:

```sh
cd webapp
yarn
```

## Running Locally

```sh
yarn dev
```

Vite starts a dev server at `http://localhost:5173` and opens it automatically. Changes to `src/` hot-reload.

## Building for Production

```sh
yarn build
```

Output goes to `webapp/dist/`. This is what gets deployed to GitHub Pages (see `.github/workflows/webapp.yml`).

To preview the production build locally:

```sh
yarn preview
```

## How It Works

On page load (`src/index.ts`):

1. `loadPyodide()` is called (script loaded from CDN in `index.html`)
2. `stationeers_pytrapic.zip` is fetched and passed to `MonacoPyrightProvider` as type stubs
3. Monaco editor is created with Python as the language
4. Pyodide finishes loading; `micropip` installs `astroid` and `luaparser` from PyPI
5. The `.whl` file is fetched and unpacked into Pyodide's in-memory filesystem
6. Initial code is loaded from URL params, `localStorage`, or a default solar-panel example
7. Editor changes trigger a debounced (500 ms) call to `compile_code` in Python via Pyodide

The compiled IC10 is syntax-highlighted using a custom `highlight.js` language definition (`src/highlight_ic10.js`).

## URL Parameters

| Param | Description |
|-------|-------------|
| `?data=<encoded>` | Load shared code+settings (base64/compressed, encoded by `types.encode_data`) |
| `?fileUrl=<url>` | Fetch raw Python source from a URL |
| `?compact=1` | Force compact output mode on load |

## Toolbar Options

| Option | Compiler flag | Default |
|--------|--------------|---------|
| Comments | `original_code_as_comment` | off |
| Compact | `compact`, `inline_functions`, `remove_labels` | off |
| Version | `append_version` | on |

## Notes

- The wheel filename in `webapp/data/` is **always** `stationeers_pytrapic-0.0.1-py3-none-any.whl` regardless of actual version — this name is hardcoded in `src/index.ts`. `build_data.sh` renames the versioned wheel when copying.
- There are no frontend tests. Testing is manual: run `yarn dev`, write Python, observe IC10 output.
- Commented-out code in `src/index.ts` (the "reload-game" / "upload-game" buttons) was intended to integrate with a local `localhost:8080` API served by the in-game C# mod. It is not currently active.
