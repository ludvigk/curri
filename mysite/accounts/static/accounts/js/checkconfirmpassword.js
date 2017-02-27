function CheckPassword() {
    var password1 = document.getElementById("password").value;
    var password2 = document.getElementById("confirm-password").value;
    
    

    if (password2=''){
        document.getElementById("confirm-password").style.backgroundColor = "#FFFFFF";
        $('#collapse-cpassword').collapse('hide')
        document.getElementById("cpassword-error").innerHTML = ""

    }
    
    if (password1=='')  {        
        document.getElementById("password").style.backgroundColor = "#FFFFFF";
        document.getElementById("confirm-password").style.backgroundColor = "#FFFFFF";
        $('#collapse-cpassword').collapse('hide')
        document.getElementById("password-error").innerHTML = ""

    }
    
    else if (password1.length < 8 || password1.length > 20) {
        document.getElementById("password").style.backgroundColor = "#f08080";
        document.getElementById("confirm-password").style.backgroundColor = "#f08080";
        document.getElementById("password-error").innerHTML = "Password must be between 8-20 characters"
	    $('#collapse-password').collapse('show')
        $('#collapse-cpassword').collapse('hide')
        document.getElementById("confirm-password").style.backgroundColor = "#FFFFFF";

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
        
        $('#collapse-password').collapse('hide')
        $('#collapse-cpassword').collapse('hide')

    }    
      
}
$('#password, #confirm-password').change(function (){CheckPassword()});
