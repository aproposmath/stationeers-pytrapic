import Notify from "simple-notify";
import "simple-notify/dist/simple-notify.css";
import * as monaco from "monaco-editor";
import { MonacoPyrightProvider } from "monaco-pyright-lsp";
import hljs from "highlight.js/lib/core";
import hljs_plain from "highlight.js/lib/languages/plaintext";
import hljs_ic10 from "./highlight_ic10";
hljs.registerLanguage("ic10", hljs_ic10);
hljs.registerLanguage("txt", hljs_plain);

import {
  createIcons,
  ClipboardPaste,
  Copy,
  Share2,
  Save,
  FolderOpen,
  RefreshCw,
  Microchip,
} from "lucide";

createIcons({
  icons: {
    ClipboardPaste,
    Copy,
    Share2,
    Save,
    FolderOpen,
    RefreshCw,
    Microchip,
  },
});

import "highlight.js/styles/github.css";

import typingUrl from "../data/stationeers_pytrapic.zip?url";
import wheelUrl from "../data/stationeers_pytrapic-0.0.1-py3-none-any.whl?url";
import workerUrl from "../node_modules/monaco-pyright-lsp/dist/worker.js?url";

function debounce(fn, delay) {
  let timer;
  const debounced = function (...args) {
    const context = this;
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(context, args), delay);
  };
  debounced.cancel = () => clearTimeout(timer);
  return debounced;
}

const defaultData = {
  code: `from stationeers_pytrapic.symbols import *

light_sensor = DaylightSensor(d0)

def handle_solar_panels():
  panels = SolarPanelDuals
  panels.Horizontal = light_sensor.Horizontal
  panels.Vertical = light_sensor.Vertical + 90

def handle_growlight():
  GrowLights.On = light_sensor.Vertical < 100

while True:
  handle_growlight()
  handle_solar_panels()
`,
  comments: true,
  compact: false,
  version: true,
};

const urlParams = new URLSearchParams(window.location.search);

let editor: monaco.editor.IStandaloneCodeEditor | null = null;
let ic10Code = "";

let gameData = {
  PythonCode: "",
  IC10Code: "",
  OldIC10Code: "",
};

function useComments() {
  return document.querySelector("#emit-comments").checked;
}

function compactOutput() {
  return document.querySelector("#compact-output").checked;
}

function appendVersion() {
  return document.querySelector("#append-version").checked;
}

let pyodide = null;
let pyodideReady = null;

const ic10Element = document.querySelector("#output") as HTMLPreElement;
const statisticsElement = document.querySelector(
  "#statistics",
) as HTMLPreElement;

async function compileCode() {
  try {
    if (editor === null) return;
    if (pyodide === null) return;

    const { code, comments, compact, append_version } = getData();

    if (code.startsWith("require")) {
      editor.getModel().setLanguage("lua");
    } else {
      editor.getModel().setLanguage("python");
    }

    ic10Element.innerHTML = "Compiling...";
    statisticsElement.innerHTML = "";
    const compileFunction = pyodide.runPython(
      `from stationeers_pytrapic.compiler import compile_code; compile_code`,
    );
    const result = compileFunction
      .callKwargs(code, { comments, compact, append_version })
      .toJs();
    if (result.error) {
      console.log("Compilation error:", result.error);
      statisticsElement.innerHTML = "";
      const stackTrace = result.stack_trace || "";
      ic10Element.innerHTML = hljs.highlight(
        result.error + "\n\n" + stackTrace,
        {
          language: "txt",
        },
      ).value;
      return;
    }
    ic10Code = result["code"];
    statisticsElement.innerHTML = `Lines: ${result.num_lines}/128, Registers: ${result.num_registers}/16, Bytes: ${result.num_bytes}`;
    ic10Element.innerHTML = hljs.highlight(result.code, {
      language: "ic10",
    }).value;
  } catch (error) {
    ic10Element.innerHTML = `Internal Error! \n\n ${error}`;
  }
}

const compileCodeDebounced = debounce(() => {
  ic10Element.innerHTML = "Compiling...";
  statisticsElement.innerHTML = "";
  compileCode();
}, 500);

function getData() {
  return {
    code: editor?.getValue() || "",
    comments: useComments(),
    compact: compactOutput(),
    append_version: appendVersion(),
  };
}

function loadData(data) {
  editor.setValue(data.code);
  document.querySelector("#emit-comments").checked = data.comments || false;
  document.querySelector("#compact-output").checked = data.compact || false;
  let appendVersion = data.version !== undefined ? data.version : true;
  document.querySelector("#append-version").checked = appendVersion;
}

async function init() {
  pyodideReady = loadPyodide();

  const typingData = await (await fetch(typingUrl)).arrayBuffer();
  const pyrightProvider = new MonacoPyrightProvider(workerUrl, {
    typeStubs: {
      stationeers_pytrapic: typingData,
    },
  });

  await pyrightProvider.init(monaco);

  editor = monaco.editor.create(
    document.querySelector("#editor") as HTMLElement,
    {
      value: "# Initializing...",
      automaticLayout: true,
      language: "python",
      fontSize: 18,
    },
  );
  pyrightProvider.setupDiagnostics(editor);

  pyodide = await pyodideReady;

  console.log("Pyodide loaded", pyodide);
  await pyodide.loadPackage("micropip");
  await pyodide.runPythonAsync(
    "import micropip; await micropip.install(['astroid', 'luaparser'])",
  );
  const wheelData = await (await fetch(wheelUrl)).arrayBuffer();
  await pyodide.unpackArchive(wheelData, "zip");

  let urlData = urlParams.get("data");
  let fileUrl = urlParams.get("fileUrl");
  if (fileUrl) {
    const code = await (await fetch(fileUrl)).text();
    loadData({ code });
  } else if (urlData) {
    const data = pyodide.runPython(
      `import stationeers_pytrapic.types; stationeers_pytrapic.decode_data`,
    )(pyodide.toPy(urlData));
    loadData(data);
  } else if (localStorage.getItem("data")) {
    loadData(JSON.parse(localStorage.getItem("data")));
  } else {
    loadData(defaultData);
  }

  editor.onDidChangeModelContent(compileCodeDebounced);

  for (const id of ["emit-comments", "compact-output", "append-version"])
    document.querySelector("#" + id)?.addEventListener("click", compileCode);

  compileCode(); // Initial compilation
}
init();

function setEditorCode(code: string) {
  if (code && editor) {
    const fullRange = editor.getModel()?.getFullModelRange();
    editor.executeEdits("paste", [
      {
        range: fullRange || new monaco.Range(1, 1, 1, 1),
        text: code,
        forceMoveMarkers: true,
      },
    ]);
    editor.pushUndoStop();
  }
}

const onClick = (id, func) => {
  document.querySelector(`#${id}`)?.addEventListener("click", func);
};

onClick("copy-ic10", () => {
  navigator.clipboard.writeText(ic10Code);
});

onClick("copy-python", () => {
  const code = editor?.getValue() || "";
  navigator.clipboard.writeText(code);
});

onClick("share", async () => {
  await pyodideReady;
  const url = new URL(window.location.href);
  const shareUrl = pyodide.runPython(
    `import stationeers_pytrapic.types; stationeers_pytrapic.encode_data`,
  )(pyodide.toPy(getData()));
  url.searchParams.set("data", shareUrl);
  navigator.clipboard.writeText(url.toString());
});

onClick("paste", () => {
  navigator.clipboard.readText().then((text) => {
    setEditorCode(text);
  });
});

onClick("save", () => {
  localStorage.setItem("data", JSON.stringify(getData()));
});

onClick("load", () => {
  loadData(JSON.parse(localStorage.getItem("data")) || defaultData);
});

onClick("reload-game", async () => {
  gameData = await (await fetch("http://localhost:8080/api/get")).json();
  if (!gameData || Object.keys(gameData).length === 0) {
    new Notify({
      title: "Error",
      text: "No chip selected in-game",
      status: "warning",
      autoclose: true,
    });
    return;
  }
  if (!gameData.PythonCode) {
    new Notify({
      title: "Info",
      text: "No Python code found in game data",
      status: "info",
      autoclose: true,
    });
  }
  if (gameData.IC10Code != gameData.OldIC10Code) {
    new Notify({
      title: "Warning",
      text: "IC10 code was changed manually. Are you sure you want to overwrite it with Python code?",
      status: "warning",
      autoclose: false,
    });
  }
  gameData.OldIC10Code = gameData.IC10Code;
  console.log("Game data loaded", gameData);
  const fullRange = editor.getModel()?.getFullModelRange();
  editor.executeEdits("paste", [
    {
      range: fullRange || new monaco.Range(1, 1, 1, 1),
      text: gameData.PythonCode || "",
      forceMoveMarkers: true,
    },
  ]);
  editor.pushUndoStop();
  //   ic10Element.innerHTML = hljs.highlight(gameData.IC10Code || "", {
  //     language: "ic10",
  //   }).value;
});

onClick("upload-game", async () => {
  gameData.PythonCode = editor.getValue();
  gameData.IC10Code = ic10Code;

  const response = await fetch("http://localhost:8080/api/upload", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(gameData),
  });
  if (response.ok) {
    console.log("Game data uploaded successfully");
    Notify({
      title: "Success",
      text: "Code uploaded successfully",
      status: "success",
      autoclose: true,
    });
  } else {
    Notify({
      title: "Error",
      text: "Failed to upload code",
      status: "error",
      autoclose: true,
    });
    console.error("Failed to upload game data", response.statusText);
  }
});
