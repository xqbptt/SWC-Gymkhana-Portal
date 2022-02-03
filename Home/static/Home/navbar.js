var defineEnterFunction = function(i) {
    return function(){
        var dropdown = document.getElementById(i+'-dropdown')
        dropdown.classList.remove('hidden')
    }
}
var defineLeaveFunction = function(i) {
    return function(){
        var dropdown = document.getElementById(i+'-dropdown')
        dropdown.classList.add('hidden')
    }
}
for(ind in board_list) {
    board_id = board_list[ind];
    var boardTab = document.getElementById('board-tab-'+board_id);
    var dropdown = document.getElementById(board_id+'-dropdown')
    if(ind<=board_list.length/2) {
        dropdown.style.left = '-100%';
    }
    else {
        dropdown.style.left = '-200%';
        dropdown.style.marginRight = '5px';
    }
    // console.log(dropdown.innerHTML)
    boardTab.onmouseenter = defineEnterFunction(board_id);
    boardTab.onmouseleave = defineLeaveFunction(board_id);
}