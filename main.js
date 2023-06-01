const path = require('path');
const {app, BrowserWindow, ipcMain, MessageChannelMain} = require('electron');
const {pythonProcess} = require("./pyProcess.js")

async function createWindow() {
    const mainWindow = new BrowserWindow({
        title: 'Mouse Yoke MOD by @matiaspedelhez', width:1120, height: 720,
        webPreferences: {
            sandbox: false,
            preload: path.join(__dirname, "./preload.js"),
          }
    });
    await mainWindow.loadFile(path.join(__dirname, './renderer/index.html'))

    return mainWindow;
}

function sendStatusMessages(mainWindow) {
  if (pythonProcess) {
    pythonProcess.stdout.on("data", function(data) {
      mainWindow.webContents.postMessage('controller_status', data);
    });
  }
}

app.whenReady().then(async () => {
    const mainWindow = await createWindow();
    sendStatusMessages(mainWindow);
  
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows() === 0){
            createWindow();
        }
    })

    app.on('quit', () => {
      process.exit();
    })
})