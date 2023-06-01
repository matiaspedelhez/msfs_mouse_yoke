const { PythonShell } = require('python-shell');

let pythonProcess = new PythonShell('./res/start.py', ["-u"]);

function requestRun(){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "RUN"}) + '\n');
}
function requestPause(){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "PAUSE"}) + '\n');
}
function requestStop(){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "FORCE_STOP"}) + '\n');
}
function requestChangeMasterKey(key){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "SET_MASTER_KEY", "input": `${key}`}) + '\n');
}
function requestChangeThrottleSensitivity(newSens){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "SET_THROTTLE_SENSITIVITY", "input": `${newSens}`}) + '\n');
}

module.exports = {requestRun, requestPause, requestStop, requestChangeMasterKey, requestChangeThrottleSensitivity, pythonProcess}