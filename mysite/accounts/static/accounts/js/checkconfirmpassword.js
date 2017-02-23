function CheckPassword() {
    var password1 = document.getElementById("password").value;
    var password2 = document.getElementById("confirm-password").value;
    
    
    
    if ((password1=='')||(password2==''))  {        document.getElementById("password").style.backgroundColor = "#FFFFFF";
    document.getElementById("confirm-password").style.backgroundColor = "#FFFFFF";

    }
    
    else if (password1.length < 8 || password1.length > 20) {
        document.getElementById("password").style.backgroundColor = "#f08080";
        document.getElementById("confirm-password").style.backgroundColor = "#f08080";
        document.getElementById("password-error").innerHTML = "Password must be between 8-20 characters"
	    $('#collapse-password').collapse('show')
    }
    
    else if (password1 != password2){
        document.getElementById("password").style.backgroundColor = "#f08080";
        document.getElementById("confirm-password").style.backgroundColor = "#f08080";
        document.getElementById("cpassword-error").innerHTML = "Passwords doesn't match"
	    
        $('#collapse-password').collapse('hide')
	    $('#collapse-cpassword').collapse('show')  
    }
    
    
    else {
        document.getElementById("password").style.backgroundColor = "#90EE90";
        document.getElementById("confirm-password").style.backgroundColor = "#90EE90";
        $('#collapse-cpassword').collapse('hide')

    }    
      
}
$('#password, #confirm-password').change(function (){CheckPassword()});
