const { contextBridge, ipcRenderer } = require("electron");

// link Python functions to object
const pythonFunctions = {
  requestRun: () => ipcRenderer.invoke("controller:run"),
};

// link status listener to object
const pythonStatus = {
  status: (callback) => ipcRenderer.on("controller_status", callback),
};

const logData = {
  text: (callback) => ipcRenderer.on("log-text", callback),
};

// send objects to frontend
contextBridge.exposeInMainWorld("pythonFunctions", pythonFunctions);
contextBridge.exposeInMainWorld("pythonStatus", pythonStatus);
contextBridge.exposeInMainWorld("logData", logData);
