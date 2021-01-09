from django.urls import path
from . import views


urlpatterns = [
	path('', views.ExtraDetailsListCreateAPIView.as_view(), name="extradetails"),
	path('<int:id>', views.ExtraDetailsAPIView.as_view(), name="extradetail"),
]
