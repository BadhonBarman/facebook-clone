var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
return new bootstrap.Tooltip(tooltipTriggerEl)
})

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
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