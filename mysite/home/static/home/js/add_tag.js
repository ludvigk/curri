
function addTag(lectureID) {
  l = 'lectureID ' + lectureID
  t = 'title ' + lectureID
  console.log(l ,t)
  $.post('/home/add_tag/', {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, lectureID: document.getElementById(l).value, title: document.getElementById(t).value},
  function(data){
    if(data=="False"){
    }
    else {
      window.location.reload()
    }
  });
}
