const Tail = require("tail").Tail;

const liveLogReader = (filePath, mainWindow) => {
  tailFile = new Tail(filePath, {
    fromBeginning: true,
    useWatchFile: true,
    fsWatchOptions: { interval: 100 },
  });

  tailFile.on("line", (data) => {
    mainWindow.webContents.postMessage("log-text", data);
  });

  tailFile.on("error", (error) => {
    console.log(error);
  });
};

module.exports = liveLogReader;
