const path = require('path');
const {app, BrowserWindow, ipcMain, win} = require('electron');
const {requestRun, requestPause} = require("./actions.js")
const { PythonShell } = require('python-shell');

let pyshell = new PythonShell('./res/start.py', ["-u"]);

function createWindow() {
    const mainWindow = new BrowserWindow({
        title: 'Mouse Yoke MOD by @matiaspedelhez', width:800, height: 500,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
          }
    });

    ipcMain.handle('requestRun', () => requestRun(pyshell))
    ipcMain.handle('requestStop', () => requestStop(pyshell))
    ipcMain.handle('requestPause', () => requestPause(pyshell))
    ipcMain.handle('requestChangeMasterKey', (key) => actions.requestChangeMasterKey(pyshell, key))
    ipcMain.handle('requestChangeThrottleSensitivity', (newSensitivity) => actions.requestChangeThrottleSensitivity(pyshell, newSensitivity))

    mainWindow.loadFile(path.join(__dirname, './renderer/index.html'))
}

app.whenReady().then( () => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows() === 0){
            createWindow()
        }
    })

    // pythonProcess = spawn('python',["-u", path.join(__dirname, './res/start.py')]);
    // console.log(path.join(__dirname, './res/start.py'))
    // pythonProcess.stdout.on('data', (data) => {
    //     console.log(data.toString())
    // });
  //   pyshell.stdout.on("data", function(data) {
  //     win.webContents.send('mouse_controller_data', data)
  // })
    pyshell.end(function (err) {
      if (err){
        throw err;
      };
      console.log('finished');
    });
    
    
})
