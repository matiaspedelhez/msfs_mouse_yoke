function requestRun(pythonProcess){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "RUN"}) + '\n');
}
function requestPause(pythonProcess){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "PAUSE"}) + '\n');
}
function requestStop(pythonProcess){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "FORCE_STOP"}) + '\n');
}
function requestChangeMasterKey(pythonProcess, key){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "SET_MASTER_KEY", "input": `${key}`}) + '\n');
}
function requestChangeThrottleSensitivity(pythonProcess, newSens){
    pythonProcess.stdin.write(JSON.stringify({"type": "request", "action": "SET_THROTTLE_SENSITIVITY", "input": `${newSens}`}) + '\n');
}

module.exports = {requestRun, requestPause, requestStop, requestChangeMasterKey, requestChangeThrottleSensitivity}