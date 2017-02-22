function register() {
	var name = $("#username").val();
	var email = $("#email").val();
	var password = $("#password").val();
	var cpassword = $("#confirm-password").val();

	var toReset = [false,false,false]

	var should_register = true

	if (name == '' || email == '' || password == '' || cpassword == '') {

	    document.getElementById("username-error").innerHTML = "All fields must be filled out"
	    $('#collapse-username').collapse('show')
		should_register = false
	}
	else if(/^[a-zA-Z0-9]*$/.test(name) == false) {
		// TOGGLE FUNKER! Må bare endre indre verdi til riktig type error.
	    //alert('Your search string contains illegal characters');
	    //$('#username-error').innerHTML = "Error"
	    //console.log($('#username-error').innerHTML)
	    document.getElementById("username-error").innerHTML = "Username contains illegal characters"
	    $('#collapse-username').collapse('show')
	    should_register = false
	}
	else if (name.length < 6 || name.length > 20) {
	    document.getElementById("username-error").innerHTML = "Username must be between 6-20 characters"
	    $('#collapse-username').collapse('show')
		should_register = false
	}

	else {
	    $('#collapse-username').collapse('hide')
	    document.getElementById("username-error").innerHTML = ""

	}

	if ((password.length) < 8 || name.length > 32) {
	    document.getElementById("password-error").innerHTML = "Password must be between 8-32 characters"
	    $('#collapse-password').collapse('show')
		should_register = false
	}

	else{
	    $('#collapse-password').collapse('hide')
	    document.getElementById("password-error").innerHTML = ""

	}
	if (!(password).match(cpassword)) {
	    document.getElementById("cpassword-error").innerHTML = "Passwords doesn't match"
	    
	    $('#collapse-cpassword').collapse('show')
		should_register = false
	}

	else{
	    $('#collapse-cpassword').collapse('hide')
	    document.getElementById("cpassword-error").innerHTML = ""

	}


	if(should_register) {
		$.get('/accounts/register/', {username: $('#username').val(), email: $('#email').val(), password: $('#password').val()},
  		function(data){

    		if(data == "True"){
      		//Redirect til register success
      		window.location.replace("/");

    		}
                console.log(data);
   		});
	}
}
$('#register-submit').click(function (){register()});
