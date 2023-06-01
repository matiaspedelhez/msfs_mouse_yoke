function run(){
    window.pythonFunctions.requestRun()
}
function stop(){
    window.pythonFunctions.requestPause()
}
function setBarValue(el_id, value){
    element = document.getElementById(el_id)
    percentage = ((value + 1) / 2) * 100

    element.style.width = percentage + "%"
}

window.pythonStatus.status((event, data) => {
    const [status] = JSON.parse(data)
    
    // update view
    document.getElementById("status-value").innerHTML = status.data.mc_status
    setBarValue("status-position-x", status.data.transformed_x)
    console.log(status)
})