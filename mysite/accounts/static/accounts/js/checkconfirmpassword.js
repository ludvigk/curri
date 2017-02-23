function CheckPassword() {
    var password1 = document.getElementById("password").value;
    var password2 = document.getElementById("confirm-password").value;
    
    if (password1.length < 8 || password1.length > 20) {
        document.getElementById("password").style.backgroundColor = "#f08080";
        document.getElementById("confirm-password").style.backgroundColor = "#f08080";

    }
    
    else if (password1 == password2){
        document.getElementById("password").style.backgroundColor = "#90EE90";
        document.getElementById("confirm-password").style.backgroundColor = "#90EE90";

    }
    else if ((password1=='')||(password2==''))  {        document.getElementById("password").style.backgroundColor = "#FFFFFF";
    document.getElementById("confirm-password").style.backgroundColor = "#FFFFFF";

    }
    else {
        document.getElementById("password").style.backgroundColor = "#f08080";
        document.getElementById("confirm-password").style.backgroundColor = "#f08080";

    }    
      
}
$('#password, #confirm-password').change(function (){CheckPassword()});
