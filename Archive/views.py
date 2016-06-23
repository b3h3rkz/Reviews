from django.shortcuts import render
from .models import Upload, Course, Student, Level, Comments
from django.views.generic import CreateView


class CommentView(CreateView):
    model = Comments
    context_object_name = 'comment'
    template_name = 'Archive/comment.html'


def home(request):
    return render(request, 'home.html')


def level_one(request):
    file_list = Upload.objects.filter(level=1).order_by('-upload_date')
    context = {'file_list': file_list}
    return render(request, 'Archive/level1.html', context)


def level_two(request):
    file_list = Upload.objects.filter(level=2).order_by('-upload_date')
    context = {'file_list': file_list}
    return render(request, 'Archive/level2.html', context)


def level_three(request):
    file_list = Upload.objects.filter(level=3).order_by('-upload_date')
    context = {'file_list': file_list}
    return render(request, 'Archive/level3.html', context)
