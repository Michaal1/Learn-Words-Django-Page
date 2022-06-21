di = false
user = document.getElementById("user")


function show(){
    let name =  document.getElementById("name");
    let logout =  document.getElementById("logout");
    if (di === false) {
        
        name.style.display = "none";
        logout.style.display = "block";
        di = true
    }
    else{
        name.style.display = "block";
        logout.style.display = "none";
        di = false
    }   
}

    

document.getElementById("user").addEventListener("click", show);

