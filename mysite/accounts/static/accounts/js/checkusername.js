function CheckUsername() {

  var myElement = document.getElementById('username');
  
  if (myElement.value == '') {
    myElement.style.backgroundColor = "White";
  }
  else if (/^[a-zA-Z0-9]*$/.test(myElement.value) == false){
    myElement.style.backgroundColor = "LightCoral";
  }
  else if (name.length < 6 || name.length > 20) {
    alert("Brukernavnet må være på mellom 6 og 20 tegn")
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
