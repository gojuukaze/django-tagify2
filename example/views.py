from django.http import HttpResponse
from django.shortcuts import render

from example.forms import TagForm, NumberForm


def index(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            return HttpResponse(str(form.cleaned_data['languages']))
    else:
        form = TagForm()
    return render(request, 'index.html', {'form': form})


def number(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['number'])
            return HttpResponse(str(form.cleaned_data['number']))

    else:
        form = NumberForm()
    return render(request, 'index.html', {'form': form})
