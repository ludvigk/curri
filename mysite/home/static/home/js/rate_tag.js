function rateTag(tagID, score) {
  $.post('/home/rate_tag/', {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, tagID: tagID, score: score},
  function(data){
    console.log(data)
    if(data=="False"){
    }
    else {
      window.location.reload()
    }
  });
}
