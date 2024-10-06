import userData from './account.js';
var createAccBtn = document.getElementById("SI_CA");
var submitBtn = document.getElementById("submit");
const email = document.getElementById("email");
const pwd = document.getElementById("SI_pwd");

createAccBtn.addEventListener('click', function(){
    window.location.href ="createAccountPage.html"
});
submitBtn.addEventListener('click', function(){
    const emVal= email.value;
    const pwdVal = pwd.value;
    var i = 0;
    var dataFound = false;
    userData.forEach(user =>{
        if(userData.email.equals(emVal) && userData.pwd.equals(pwdVal)){
            if(userData.accType.equals("Shopper")){
                window.location.href = "userAccountPage.html"
            }else{
                window.location.href = "busAccountPage.html"
            }
            dataFound = true;
        }
        else{
            i++;
        }
    });
    
    if(!dataFound){
        prompt("Please try again or Create an Account");
    }

});