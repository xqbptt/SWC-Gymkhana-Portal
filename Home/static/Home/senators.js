console.log("Senator script is running");
panel_list = JSON.parse(panel_list)
console.log(panel_list)
var currentActiveTabIndex = 0;
var currentActiveButton = document.getElementById("senator-button-"+currentActiveTabIndex)
var currentActiveTab = document.getElementById("senator-tab-"+currentActiveTabIndex)
currentActiveButton.classList.remove("bg-white")
currentActiveButton.classList.add("bg-black")
currentActiveButton.classList.remove("text-black")
currentActiveButton.classList.add("text-white")
currentActiveTab.classList.remove('hidden')
var defineFunction = function(i){
    return function(){
        var currentActiveButton = document.getElementById("senator-button-"+currentActiveTabIndex)
        var currentActiveTab = document.getElementById("senator-tab-"+currentActiveTabIndex)
        var button = document.getElementById("senator-button-"+i)
        var tab = document.getElementById("senator-tab-"+i)
        currentActiveButton.classList.remove("bg-black")
        currentActiveButton.classList.add("bg-white")
        currentActiveButton.classList.remove("text-white")
        currentActiveButton.classList.add("text-black")
        button.classList.remove("bg-white")
        button.classList.add("bg-black")
        button.classList.remove("text-black")
        button.classList.add("text-white")
        currentActiveTab.classList.add('hidden')
        tab.classList.remove('hidden')
        currentActiveTabIndex=i
    }
}
for(var i = 0; i<panel_list.length; i++) {
    var button = document.getElementById("senator-button-"+i)
    button.onclick = defineFunction(i)
}