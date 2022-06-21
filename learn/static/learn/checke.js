// Program opravi chybne slovicka a po 800ms zobrazi spravnu podobu

var script = document.getElementById("id");
var data = script.value;

    
var obj = JSON.parse(data)
console.log(obj)


function checkKey(e) {
    e = e || window.event;
    if (e.keyCode == '13') {
        document.getElementById('nxt').click();
    }
}

document.addEventListener('keydown',checkKey);


setTimeout(function () {
    try{
        document.getElementById("in_1").value = obj.a;
        document.getElementById("in_2").value = obj.b;
        document.getElementById("in_3").value = obj.c;
        document.getElementById("in_4").value = obj.d;
      }
      catch{
        document.getElementById("in_t").value = obj.a;
        document.getElementById("in_tt").value = obj.b;
      }
}, 800);






