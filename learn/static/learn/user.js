// Program zobrazuje tlacitko logout po prejdeni na ikonku pouzivatela
logoutButton = false // False - logout button je skryty
user = document.getElementById("user")


function show(){
    let name =  document.getElementById("name");
    let logout =  document.getElementById("logout");
    if (logoutButton === false) {
        
        name.style.display = "none";
        logout.style.display = "block";
        logoutButton = true
    }
    else{
        name.style.display = "block";
        logout.style.display = "none";
        logoutButton = false
    }   
}

    

document.getElementById("user").addEventListener("click", show);

