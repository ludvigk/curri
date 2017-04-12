function addSubject() {
  $.post('/home/add_subject/', {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, subjectID: document.getElementById('subjectID').value},
  function(data){
    console.log(data)
    if(data=="No such subject"){
    }
    else {
      window.location.replace('/home/')
    }
  });
}
