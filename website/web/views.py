from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Post
# Create your views here.
def login(request):
	if request.user.is_authenticated:
		return render(request,'home.html')
	if request.method=="POST":
		username=request.POST['USERNAME']
		password=request.POST['PASSWORD']
		user=auth.authenticate(password=password,username=username)
		if user is not None:
			auth.login(request,user)
			return redirect("home")
		else:
			messages.info(request,"INVALID CREDENTIALS")
			print("INVALID")
			return redirect("/")	
	else:
		return render(request,'login.html')
def register(request):
	if request.method=="POST":
		username=request.POST['USERNAME']
		password1=request.POST['PASSWORD2']
		password2=request.POST['PASSWORD2']
		firstname=request.POST['FIRSTNAME']
		lastname=request.POST['LASTNAME']
		email=request.POST['EMAIL']
		if password2==password1:
			if User.objects.filter(username=username).exists():
				messages.info(request,"USERNAME TAKEN")
				print("email")
			elif User.objects.filter(email=email).exists():
				messages.info(request,"EMAIL ALREADY TAKEN")
				print("email")
			else:		
				print("OOO")
				user=User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname,email=email)
				user.save()
				auth.login(request,user)
				print("TRIESs")
				return redirect('home')
				print("POPPY")
		else:
			messages.info(request,"PASSWORD NOT CORRECT")
			return redirect('register')					
	return render(request,"register.html")		
def home(request):
	if request.user.is_authenticated:
		l=Post.objects.all()
		context={'POST':l}
		return render(request,'home.html',context)
	else:
		return redirect('/')				
def logout(request):
	auth.logout(request)
	return redirect('/')
def post(request):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method=="POST":
		tilte=request.POST["TITLE"]
		description=request.POST["DESCRIPTION"]
		user=request.user
		print(user)
		if tilte=="":
			messages.info(request,"TITLE IS REQUIRED")
			return redirect('post')
		if description=="":
			messages.info(request,"DESCRIPTION IS REQUIRED")
			return redirect('post')				
		pod=Post(title=tilte,user=request.user,description=description)
		pod.save()
		return redirect('home')
	if  request.user.is_authenticated:
		return render(request,'post.html')



