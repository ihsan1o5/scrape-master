from django.shortcuts import render, redirect
from django.views import View 
from .models import User 
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth 
from datetime import timedelta

# Create your views here.

class RegisterationView(View):
	def get(self, request):
		return render(request, 'authentication/signup.html')

	def post(self, request):
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		password1 = request.POST['password1']

		context = {
			'formData': request.POST
		}

		if not User.objects.filter(username=username).exists():
			if not User.objects.filter(email=email).exists():
				if password != password1:
					messages.error(request, 'Passwords not matching')
					return render(request, 'authentication/signup.html', context)
				else:
					user = User.objects.create_user(username=username, email=email)
					user.set_password(password)
					user.save()

					t_user = User.objects.get(email=email)

					token = RefreshToken.for_user(t_user)
					access_token = token.access_token
					access_token.set_exp(lifetime=timedelta(days=360))

					messages.success(request, 'A user with the username '+str(username)+' is registered successfully!')
					return redirect('dashboard-home')
			else:
				messages.error(request, 'A user is already registered at this email, Please use another')
				return render(request, 'authentication/signup.html', context)
		else:
			messages.error(request, 'Username already taken!')
			return render(request, 'authentication/signup.html', context)

class LoginView(View):
	"""docstring for LoginView"""
	def get(self, request):
		return render(request, 'authentication/login.html')
		
	def post(self, request):
		
		email = request.POST['email']
		password = request.POST['password']

		if email and password:
			user = auth.authenticate(email=email, password=password)
			if user:
				if user.is_active:
					auth.login(request, user)

					t_user = User.objects.get(email=email)
					tokens = t_user.tokens()
					print(tokens)
					messages.success(request, 'Welcom '+str(user.username)+' Your are now loged in')
					return redirect('dashboard-home')
				else:
					messages.error(request, 'Sorry '+str(user.username)+' Your acount is set to unactive for some reason please contact with administration office')
			else:
				messages.error(request, 'User not exists! Please create your account first')
		else:
			messages.error(request, 'Email and Password both are required!')
		return render(request, 'authentication/login.html')

		
def logout(request):
	auth.logout(request)
	messages.success(request, 'Loged Out successfully!')
	return redirect('login')

		

