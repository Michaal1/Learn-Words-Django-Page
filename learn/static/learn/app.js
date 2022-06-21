 // Program meni focus na jednotlive okienka formularu podla stlacania sipok
var one = ""
var two = ""
var three = ""
var four = ""
var active = 0;
function getFocus(idd) {// Funkcia nastavi focus podla id formularu
    document.getElementById(idd).focus();
  }

function checkKey(e) { // Funkcia nastavuje formular na ktory sa bude davat focus podla pohybu sipkami
    e = e || window.event;
    try {
        var el = document.querySelector('#in_1');
        if ((el === document.activeElement) === true) {
            active = 1
        }
        el = document.querySelector('#in_2');
        if ((el === document.activeElement) === true ){
            active = 2
        }
        el = document.querySelector('#in_3');
        if ((el === document.activeElement) === true) {
            active = 3
        }
        el = document.querySelector('#in_4');
        if ((el === document.activeElement) === true) {
            active = 4
        }
        if (e.keyCode == '37') {
            // left arrow
            active = active - 1
            console.log(active)

            if(active<1) {
                active = 4
                console.log(active)
            }
        }
        else if (e.keyCode == '39') {
            // right arrowif 
            active = active + 1
            console.log(active)
            if(active>4) {
                active = 1
                console.log(active)
            }
                
        }
        if (active===1) {
            getFocus("in_1")
        }
        else if (active===2) {
            getFocus("in_2")
        }
        else if (active===3) {
            getFocus("in_3")
        }
        else if (active===4) {
            getFocus("in_4")
        }
    }
    catch{
        var el = document.querySelector('#in_t');
        if ((el === document.activeElement) === true) {
            active = 1
        }
        el = document.querySelector('#in_tt');
        if ((el === document.activeElement) === true ){
            active = 2
        }
        if (e.keyCode == '37') {
            // left arrow
            active = active - 1
            console.log(active)

            if(active<1) {
                active = 2
                console.log(active)
            }
        }
        else if (e.keyCode == '39') {
            // right arrowif 
            active = active + 1
            console.log(active)
            if(active>2) {
                active = 1
                console.log(active)
            }
        }
        if (active===1) {
            getFocus("in_t")
        }
        else if (active===2) {
            getFocus("in_tt")
        }
    }
    
    
    
    
}
try{
    getFocus("in_1")
}
catch{
    getFocus("in_t")
}

document.addEventListener('keydown',checkKey); // Kontrola stlacenia klavesu spusti funkciu "checkKey"
