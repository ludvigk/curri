function CheckUsername() {

  var myElement = document.getElementById('username');

  if (myElement.value == '') {
    myElement.style.backgroundColor = "White";
  }
  else if (myElement.length < 6 || myElement.length > 20) {
    myElement.style.backgroundColor = "LightCoral";
  }
  else if (/^[a-zA-Z0-9]*$/.test(myElement.value) == false){
    myElement.style.backgroundColor = "LightCoral";
  }
  else {
    $.get('/accounts/checkusername/', {username: $('#username').val()},
    function(data){ 

      if(data == "True"){
        myElement.style.backgroundColor = "LightGreen";
      } 
      else {
        myElement.style.backgroundColor = "LightCoral";
      }
    });
  }
}
$('#username').change(function (){CheckUsername()});
