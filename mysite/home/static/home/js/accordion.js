$(document).ready(function() {
  
  var lastState = localStorage.getItem('lastState');

  if (!lastState) {
    lastState = [];
    localStorage.setItem('lastState', JSON.stringify(lastState));
  } else {
    lastStateArray = JSON.parse(lastState);
    var arrayLength = lastStateArray.length;
    for (var i = 0; i < arrayLength; i++) {
        var panel = '#'+lastStateArray[i];
        $(panel).addClass('in');
    }
  }

  $(document).on('shown.bs.collapse', '.panel-collapse', function() {
    lastState = JSON.parse(localStorage.getItem('lastState'));
    if ($.inArray($(this).attr('id'), lastState) == -1) {
        lastState.push($(this).attr('id'));
    };
    localStorage.setItem('lastState', JSON.stringify(lastState));
  });

  $(document).on('hidden.bs.collapse', '.panel-collapse', function() {
    lastState = JSON.parse(localStorage.getItem('lastState'));
    lastState.splice( $.inArray($(this).attr('id'), lastState), 1 ); 
    localStorage.setItem('lastState', JSON.stringify(lastState));
  });

});

var retainStateArray = JSON.parse(localStorage.getItem('lastState'));
console.log(retainStateArray)
var arrayLength = retainStateArray.length;
for (var i = 0; i < arrayLength; i++) {
    var panel = '#'+retainStateArray[i];
    $(panel).addClass('in');
    console.log(panel);
}
