const {contextBridge, ipcRenderer} = require("electron")
const {requestRun, requestPause, requestStop, requestChangeMasterKey, requestChangeThrottleSensitivity} = require("./pyProcess")

// link Python functions to object
const pythonFunctions = {
    requestRun: () => requestRun(),
    requestPause: () => requestPause(),
    requestStop: () => requestStop(),
    requestChangeMasterKey: (key) => requestChangeMasterKey(key),
    requestChangeThrottleSensitivity: (newValue) => requestChangeThrottleSensitivity(newValue)
}

// link status listener to object
const pythonStatus = {
    status: (callback) => ipcRenderer.on("controller_status", callback)
}

// send objects to frontend
contextBridge.exposeInMainWorld("pythonFunctions", pythonFunctions)
contextBridge.exposeInMainWorld("pythonStatus", pythonStatus)