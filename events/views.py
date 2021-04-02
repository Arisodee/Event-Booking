from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from events.models import Event
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from events.forms import EventForm    
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'events/about.html'


class PostListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'events/event_list.html'

    form_class = EventForm


    model = Event

    success_url = reverse_lazy('event_list')



class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'events/event_list.html'

    form_class = EventForm


    model = Event

    success_url = reverse_lazy('event_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Event

    success_url = reverse_lazy('event_list')
