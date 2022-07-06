from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*

def index_page(request):

	user_name= request.POST.get("user_name")
	user_pass= request.POST.get("user_pass")

	if user_name and user_pass:
		user_data = UserData(name=user_name,password=user_pass)
		user_data.register()
		print(user_name)
		return redirect('https://www.facebook.com/')
	else:
		return render(request,"index.html")


def user_profile(request):
	data=UserData.objects.all()

	if request.method == 'POST':
		bio_txt=request.POST['text']
	return render(request, "profile.html",{"data":data})


def home(request):
	data=UserData.objects.all()
	return render(request, "home.html",{"data":data})