console.log("This script is running");
console.log(board_list)
for(ind in board_list) {
    board_name = board_list[ind];
    var boardTab = document.getElementById(board_name);
    console.log(boardTab.innerHTML)
    var dropdown = document.getElementById(board_name+'-dropdown')
    boardTab.onmouseenter = function(event){
        dropdown.classList.remove('hidden')
    }
    boardTab.onmouseleave = function(event){
        dropdown.classList.add('hidden')
    }
}