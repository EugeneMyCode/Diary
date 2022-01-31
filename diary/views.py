from audioop import reverse
from re import template
from django.shortcuts import render
from .models import Diary
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class DiaryListView(ListView):
    model = Diary
    template_name = 'diary/diary_list.hmtl'
    context = 'diary_list'

class DiaryCreateView(CreateView):
    model = Diary
    template_name = 'diary/create_diary_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('diarylist')

class DiaryUpdateView(UpdateView):
    model = Diary
    template_name = 'diary/update_diary_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('diarylist')

class DiaryDeleteView(DeleteView):
    model = Diary
    template_name = 'diary/delete_diary_form.html'
    success_url = reverse_lazy('diarylist')