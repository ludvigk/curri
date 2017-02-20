function register() {
	var name = $("#name").val();
	var email = $("#email").val();
	var password = $("#password").val();
	var cpassword = $("#confirm-password").val();

	if (name == '' || email == '' || password == '' || cpassword == '') {
		alert("Fyll ut alle felter");
	} 
	else if ((password.length) < 8) {
		alert("Passord må være minst 8 karakterer langt");
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
  
   		});
	}

}
$('#register-submit').click(function (){register()});