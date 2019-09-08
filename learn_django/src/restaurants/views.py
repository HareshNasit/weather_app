from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
# Create your views here.

class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    #success_url = '/restaurants/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'
    #success_url = '/restaurants/'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        name = self.get_object().name
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = f'Update Restaurant: {name}'
        return context

# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         context = {
#         }
#         return context
#
# class AboutView(TemplateView):
#     template_name = 'about.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(AboutView, self).get_context_data(*args, **kwargs)
#         restaurants = ["Rowa", "Rotana", "Roti N Boti", "Papa Johns"]
#         lucky_num = 12
#         context = {
#             "restaurants": restaurants,
#             "lucky_num": lucky_num
#         }
#         return context
#
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ContactView, self).get_context_data(*args, **kwargs)
#         context = {
#         }
#         return context
