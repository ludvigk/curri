function create_subject() {
  console.log("hello")
  $.get('/home/create_subject/', 
    {'subject': $('#subject').val(),
     'subject_code': $('#subject_code').val()},
  function(data){
    console.log("lols")
    return;
  });
  console.log("works")
}
$('#create_subject_btn').click(function(){create_subject()});
