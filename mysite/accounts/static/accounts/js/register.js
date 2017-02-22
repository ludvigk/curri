function register() {
	var name = $("#username").val();
	var email = $("#email").val();
	var password = $("#password").val();
	var cpassword = $("#confirm-password").val();

	if (name == '' || email == '' || password == '' || cpassword == '') {
		alert("Fyll ut alle felter");
	}
	else if(/^[a-zA-Z0-9]*$/.test(name) == false) {
		// TOGGLE FUNKER! Må bare endre indre verdi til riktig type error.
	    //alert('Your search string contains illegal characters');
	    //$('#collapse-username').getElementByTagName('p').innerHTML = "Error"
	    $('#collapse-username').collapse('toggle')
	}
	else if (name.length < 6 || name.length > 20) {
		alert("Brukernavnet må være på mellom 6 og 20 tegn")
	}
	else if ((password.length) < 8 || name.length > 32) {
		alert("Passord må være mellom 8-32 karakterer langt");
	} 
	else if (!(password).match(cpassword)) {
		alert("Passord matcher ikke");
	} 
	else {
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
