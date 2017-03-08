function create_subject() {
  $.get('/home/create_subject/', 
    {subject: $('#subject').val(),
     subject_code: $('#subject_code').val()},
  function(data){
    $('#createModal').modal('hide');
  });
}
$('#create_subject_btn').click(function(){create_subject()});
