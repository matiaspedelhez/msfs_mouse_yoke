const {ipcRenderer} = require('electron');

async function run() {
    await ipcRenderer.invoke('requestRun')
}
async function stop()  {
    await ipcRenderer.invoke('requestStop')
}

console.log('hello')