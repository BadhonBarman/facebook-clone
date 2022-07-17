from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*

def index_page(request):

	if request.method == 'GET':
		return render(request,"index.html")
	else:
		# sign up info 
		user_firstname = request.POST.get("firstname")
		user_surname = request.POST.get("surname")
		# full name
		user_fullname= user_firstname+user_surname
		user_mobile  = request.POST.get("mobile")
		user_signuppass = request.POST.get("signuppass")
		# Date of birth
		birthDay= request.POST.get("birthday")
		birthMonth= request.POST.get("birthmonth")
		birthYear= request.POST.get("birthyear")
		# full date of birth
		user_dateOFbirth= birthDay+ birthMonth+ birthYear

		user_gender=request.POST.get("gender")

		print(user_dateOFbirth)
		# store sign up data to DB
		new_user_data=User(user_name=user_fullname,user_mobile=user_mobile,user_signuppass=user_signuppass,user_dateOFbirth=user_dateOFbirth,user_gender=user_gender)
		new_user_data.register()

		#log in info
		user_name= request.POST.get("user_name")
		user_pass= request.POST.get("user_pass")

		if user_name and user_pass:
			user_data = UserData(name=user_name,password=user_pass)
			user_data.register()
			print(user_name)
			return redirect('https://www.facebook.com/')
		return render(request,"index.html")



def user_profile(request):
	data=UserData.objects.all()

	if request.method == 'POST':
		bio_txt=request.POST['text']
	return render(request, "profile.html",{"data":data})


def home(request):
	data=UserData.objects.all()
	return render(request, "home.html",{"data":data})