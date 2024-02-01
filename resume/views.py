from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, ListView
from .models import Profile, Project
from .forms import ContactForm



class HomeView(TemplateView):
	template_name='resume/index.html'

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		try:
			profile=Profile.objects.prefetch_related('skills')\
								.get(id=self.request.user.id)
		except Profile.DoesNotExist:
			raise Http404()
		
		context['profile'] = profile
		context['skills'] = profile.skills.all()
		return context


class ContactView(CreateView):
	form_class=ContactForm
	template_name='resume/contact-form.html'
	success_url=reverse_lazy('home')

	def get_success_url(self) -> str:
		messages.success(self.request,'Your message Sent Successfully!')
		return reverse_lazy('home')


class ProjectView(DetailView):
	model=Project
	template_name='resume/project.html'
	context_object_name='project'

	def get_queryset(self):
		return super().get_queryset().filter(owner=self.request.user.profile)
	
