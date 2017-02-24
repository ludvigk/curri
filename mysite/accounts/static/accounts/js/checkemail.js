function CheckEmail() {
  var myElement = document.getElementById('email');
  re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (myElement.value == "") {
    myElement.style.backgroundColor = "White";
    $('#collapse-email').collapse('hide')
    document.getElementById("email-error").innerHTML = ""
  }
  else if (!myElement.value.match(re)){
    myElement.style.backgroundColor = "LightCoral";
    document.getElementById("email-error").innerHTML = "Invalid email"
    $('#collapse-email').collapse('show')
  }
  else {
    $.get('/accounts/checkemail/', {email: $('#email').val()},
    function(data){
      if(data == "True") {
        myElement.style.backgroundColor = "LightGreen";
        document.getElementById("email-error").innerHTML = ""
        $('#collapse-email').collapse('hide')
      }
      else {
        myElement.style.backgroundColor = "LightCoral";
        document.getElementById("email-error").innerHTML = "An account is already registered with this email"
        $('#collapse-email').collapse('show')
      }
    });
  }
}
$('#email').change(function (){CheckEmail()});
