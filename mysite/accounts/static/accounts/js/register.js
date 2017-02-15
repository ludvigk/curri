function register() {
  $.get('/accounts/register/', {username: $('#username').val(), email: $('#email').val(), password: $('#password').val()},
  function(data){

    if(data == "True"){
      //Redirect til register success
      window.location.replace("/");

    }
  
  });
}
$('#register-submit').click(function (){register()});