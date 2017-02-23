function CheckPassword() {
    var password1 = document.getElementById("id_new_password1");
    var password2 = document.getElementById("id_new_password2");

    if ((password1.value == '') || (password2.value == ''))  {
        password1.style.backgroundColor = "White";
        password2.style.backgroundColor = "White";
    }
    else if (password1.value.length < 8 || password1.value.length > 20) {
        password1.style.backgroundColor = "#f08080";
        password2.style.backgroundColor = "#f08080";
        document.getElementById("password-error").innerHTML = "Password must be between 8-20 characters"
        $('#collapse-password').collapse('show')
        $('#collapse-cpassword').collapse('hide')
    }
    else if (password1.value != password2.value){
        password1.style.backgroundColor = "#f08080";
        password2.style.backgroundColor = "#f08080";
        document.getElementById("cpassword-error").innerHTML = "Passwords do not match"
        $('#collapse-password').collapse('hide')
        $('#collapse-cpassword').collapse('show')
    }
    else {
        password1.style.backgroundColor = "#90EE90";
        password2.style.backgroundColor = "#90EE90";
        $('#collapse-password').collapse('hide')
        $('#collapse-cpassword').collapse('hide')
    }
}
$('#id_new_password1, #id_new_password2').change(function (){CheckPassword()});
