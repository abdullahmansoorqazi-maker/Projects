function login(){

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if(username === "Code Technologist" && password === "bsse"){

        localStorage.setItem("login","true");

        window.location.href = "dashboard.html";
    }
    else{
        alert("Wrong Username or Password");
    }
}