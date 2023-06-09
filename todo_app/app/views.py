from django.shortcuts import render,redirect
from django.http import HttpResponse
from .froms import CreateForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Create

# Create your views here.
class index(CreateView):
    model = Create
    form_class = CreateForm
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = self.model.objects.all()
        return context
    
class update(UpdateView):
    model = Create
    template_name = 'update.html'
    success_url = '/'
    fields ={
        'title',
        'complete'
    }

class delete(DeleteView):
    model = Create
    template_name = 'delete.html'
    success_url = '/'
   