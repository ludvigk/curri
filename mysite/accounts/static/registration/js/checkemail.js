function CheckEmail() {
  var myElement = document.getElementById('id_email');
  re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (myElement.value == "") {
    myElement.style.backgroundColor = "White";
    console.log("test")
  } else if(!myElement.value.match(re)) {
    myElement.style.backgroundColor = "LightCoral";
    document.getElementById("email-error").innerHTML = "Not a valid email"
    $('#collapse-email').collapse('show')
  } else {
    myElement.style.backgroundColor = "LightGreen";
    document.getElementById("email-error").innerHTML = ""
    $('#collapse-email').collapse('hide')
  }
}
$('#id_email').change(function (){CheckEmail()});
