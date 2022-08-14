from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*

def index_page(request):
	return render(request,"index.html")


def SignUp(request):
	#sign up info 
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
	new_user_data=User(user_name=user_fullname,user_phone=user_mobile,user_signuppass=user_signuppass,user_dateOFbirth=user_dateOFbirth,user_gender=user_gender)
	new_user_data.register()
	return redirect('index')


def user_profile(request):
	if request.method =='POST':
		user_phone= request.POST.get("user_phone_number")
		user_pass= request.POST.get("user_pass")
		error_txt =None
		get_user= User.login_user_by_phone(user_phone)

		if get_user:
			if user_pass == get_user.user_signuppass:
				request.session['name']=get_user.user_name
				request.session['phone']=get_user.user_phone
				return redirect('profile')
			else:
				pass 
		else:
			print("restriction working")

	user_phone_id = request.session['phone']
	data=User.objects.filter(user_phone=user_phone_id)
	return render(request, "profile.html",{"data":data})	


def home(request):
	data=UserData.objects.all()
	return render(request, "home.html",{"data":data})