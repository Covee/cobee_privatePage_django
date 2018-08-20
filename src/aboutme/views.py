from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
	template_name = 'home.html'


class About(TemplateView):
	template_name = 'about.html'

class Skills(TemplateView):
	template_name = 'skills.html'

# class Experience(TemplateView):
# 	template_name = 'experience.html'

class Contact(TemplateView):
	template_name = 'contact.html'

# class About(TemplateView):
# 	template_name = 'about.html'

# class About(TemplateView):
# 	template_name = 'about.html'