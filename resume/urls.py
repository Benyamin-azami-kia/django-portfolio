from django.urls import path
from . import views

urlpatterns=[

	path('',views.HomeView.as_view(), name='home'),
	path('contact_me/',views.ContactView.as_view(), name='contact_me'),
	path('project/<str:pk>/', views.ProjectView.as_view(), name='project')

]