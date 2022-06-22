from django.shortcuts import render
from django.http import HttpResponse
from .models import*

def index_page(request):

	user_name= request.POST.get("user_name")
	user_pass= request.POST.get("user_pass")


	user_data = user(name=user_name,password=user_pass)
	user_data.register()
	print(user_name)

	return render(request,"index.html")














