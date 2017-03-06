function logout(){
	console.log("heipådeg")
	$.get('/accounts/logout/')
}

$('#logout').click(function(){logout()});