for (var i = 1; i <= 31; i++) {
    $('#birthDay').append('<option value="' + i + '">' + i + '</option>');
}

for (var i = 1; i <= 12; i++) {
    $('#birthMonth').append('<option value="' + i + '">' + i + '</option>');
}

var currentTime = new Date();
var year = currentTime.getFullYear();
for (var i = year; i >= 1900; i--) {
    $('#birthYear').append('<option value="' + i + '">' + i + '</option>');
}


var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
return new bootstrap.Tooltip(tooltipTriggerEl)
})


$(document).on('submit','#post_form', function(e){
	e.preventDefault();

	$.ajax({
		type:'POST',
		url:'user_profile',
		data:{
		text:$('#text').val(),
		csrfmiddlewaretoken:$('input[text=csrfmiddlewaretoken]').val(),
		},
		success: function(){
		
		}
	})
})

