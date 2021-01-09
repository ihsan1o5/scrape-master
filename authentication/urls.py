from django.urls import path
from . import views
from .views import RegisterationView, LoginView

urlpatterns = [
	path('', LoginView.as_view(), name='login'),
	path('signup/', RegisterationView.as_view(), name='signup'),
	path('logout/', views.logout, name='logout'),
]