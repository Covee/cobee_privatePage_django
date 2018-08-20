from django.urls import path
from .views import MainView, About, Skills, Contact


urlpatterns = [
	path('', MainView.as_view(), name='home'),
	path('about/', About.as_view(), name='about'),
	path('skills/', Skills.as_view(), name='skills'),
	path('contact/', Contact.as_view(), name='contact'),
	# path('', MainView.as_view(), name='home'),

]