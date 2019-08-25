from django.shortcuts import render
from django.views.generic.base import TemplateView
from . models import Article
# Create your views here.

class Home(TemplateView):
	template_name = 'home/home.html'
	article = Article.objects.first_articles()
	
	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/index_hero.jpg'
		context["active_page"] = 'home'
		context["article"] = self.article
		return context

class Services(TemplateView):
	template_name = 'home/services.html'
	
	
	def get_context_data(self, *args, **kwargs):
		context = super(Services, self).get_context_data(*args, **kwargs)		
		context["bck_image"] = 'images/services.jpg'
		context["active_page"] = 'services'
		return context