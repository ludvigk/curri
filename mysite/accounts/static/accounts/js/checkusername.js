function CheckUsername() {

  var myElement = document.getElementById('username');
  if (myElement.value == '') {
    myElement.style.backgroundColor = "White";
  }
    
  else if (myElement.value.length < 4 || myElement.value.length > 20) {
    myElement.style.backgroundColor = "LightCoral";
    document.getElementById("username-error").innerHTML = "Username must be between 4-20 characters"
    $('#collapse-username').collapse('show')
  }
    
  else if (/^[a-zA-Z0-9]*$/.test(myElement.value) == false){
    myElement.style.backgroundColor = "LightCoral";
    document.getElementById("username-error").innerHTML = "Username contains illegal characters"
    $('#collapse-username').collapse('show')
  }
    
  else {
    $('#collapse-username').collapse('hide')
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
