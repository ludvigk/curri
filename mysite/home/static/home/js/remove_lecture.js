function removeLecture(subjectID) {
  $.post('/home/remove_lecture/' + document.getElementById('subjectID').value + '/', {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, lectureID: document.getElementById('lectureID').value},
  function(data){
    if(data=="False"){
    }
    else {
      window.location.reload(true)
    }
  });
}
