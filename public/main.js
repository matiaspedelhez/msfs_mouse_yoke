const { app, BrowserWindow, ipcMain } = require("electron");
// const { pythonProcess } = require("./pyProcess.js");
const { PythonShell } = require("python-shell");
const date = require("date-and-time");
const path = require("path");
const isDev = require("electron-is-dev");

// Retrieve date for log naming
const now = new Date();
const logName = date.format(now, "MMDD-hh-mm-ss-ms");

// Initiate Python process
const pyProcess = new PythonShell("start.py", {
  pythonOptions: ["-u"],
  args: [logName],
  scriptPath: path.join(__dirname, "../res"),
});

let mainWindow;

async function createWindow() {
  mainWindow = new BrowserWindow({
    title: "Mouse Yoke MOD by @matiaspedelhez",
    width: 1120,
    height: 720,
    maximizable: false,
    resizable: false,
    webPreferences: {
      sandbox: false,
      preload: path.join(__dirname, "./preload.js"),
    },
  });
  mainWindow.loadURL(
    isDev
      ? "http://localhost:3000"
      : `file://${path.join(__dirname, "../build/index.html")}`
  );
  mainWindow.setMenuBarVisibility(false);
  mainWindow.on("closed", () => (mainWindow = null));

  // Expose Python Functions
  ipcMain.handle("controller:run", requestRun);
}

function sendStatusMessages(mainWindow) {
  pyProcess.stdout.on("data", function (data) {
    mainWindow.webContents.postMessage("controller_status", data);
  });
}

app.whenReady().then(() => {
  createWindow();
  sendStatusMessages(mainWindow);

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows() === 0) {
      createWindow();
    }
  });

  app.on("quit", () => {
    process.exit();
  });
});

// Functions to interactuate with Python
function requestRun() {
  pyProcess.stdin.write(
    JSON.stringify({ type: "request", action: "RUN" }) + "\n"
  );
}

function requestPause() {
  pyProcess.stdin.write(
    JSON.stringify({ type: "request", action: "PAUSE" }) + "\n"
  );
}

function requestStop() {
  pyProcess.stdin.write(
    JSON.stringify({ type: "request", action: "FORCE_STOP" }) + "\n"
  );
}

function requestChangeMasterKey(key) {
  pyProcess.stdin.write(
    JSON.stringify({
      type: "request",
      action: "SET_MASTER_KEY",
      input: `${key}`,
    }) + "\n"
  );
}

function requestChangeThrottleSensitivity(newSens) {
  pyProcess.stdin.write(
    JSON.stringify({
      type: "request",
      action: "SET_THROTTLE_SENSITIVITY",
      input: `${newSens}`,
    }) + "\n"
  );
}
