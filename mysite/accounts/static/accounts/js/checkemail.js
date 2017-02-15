function CheckEmail() {
  $.get('/accounts/checkemail/', {email: $('#email').val()},
  function(data){
    var myElement = document.getElementById('email');
    if (myElement.value == '') {
      myElement.style.backgroundColor = "White";
    } else if(data == "True") {
      myElement.style.backgroundColor = "LightGreen";
    } else {
      myElement.style.backgroundColor = "LightCoral";
    }
  });
}
$('#email').change(function (){CheckEmail()});
