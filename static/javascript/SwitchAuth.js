let loginDiv = document.getElementById("loginDivID");
let registerDiv = document.getElementById("registerDivID");

document.getElementById("switchLogin").addEventListener("click", ()=>{
    registerDiv.style.display = "none";
    loginDiv.style.display = "flex";
})

document.getElementById("switchRegister").addEventListener("click", ()=>{
    loginDiv.style.display = "none";
    registerDiv.style.display = "flex";
})
