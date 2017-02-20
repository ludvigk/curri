function register() {
  console.log("hello");
  $.get('/accounts/register/', {username: $('#username').val(), email: $('#email').val(), password: $('#password').val(), confirm_password: $('#confirm-password').val()},
  function(data){
    if(data == "True"){
      //Redirect til register success
      window.location.replace("/");

    } else {
      //
    }
  });
}
$('#register-submit').click(function (){register()});
