function CheckUsername() {
  $.get('/accounts/checkusername/', {username: $('#username').val()},
  function(data){
    var myElement = document.getElementById('username');
    if (myElement.value == '') {
      myElement.style.backgroundColor = "White";
    } else if(data == "True"){
      myElement.style.backgroundColor = "LightGreen";
    } else {
      myElement.style.backgroundColor = "LightCoral";
    }
  });
}
$('#username').change(function (){CheckUsername()});
