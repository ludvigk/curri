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
	    should_register = false
	}
	else if (name.length < 4 || name.length > 20) {
		should_register = false
	}

	else {
	    document.getElementById("username-error").innerHTML = ""

	}

	if ((password.length) < 8 || name.length > 20) {
		should_register = false
	}

	else{
	    document.getElementById("password-error").innerHTML = ""

	}
	if (!(password).match(cpassword)) {
		should_register = false
	}

	else{
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
