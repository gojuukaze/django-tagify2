from django.http import HttpResponse
from django.shortcuts import render

from example.forms import TagForm, dataListFuncTestForm


def index(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['fruits'])
            return HttpResponse(str(form.cleaned_data['fruits']))

    else:
        form = TagForm()
    return render(request, 'index.html', {'form': form})


def data_list_func_test(request):
    if request.method == 'POST':
        form = dataListFuncTestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['number'])
            return HttpResponse(str(form.cleaned_data['number']))

    else:
        form = dataListFuncTestForm()
    return render(request, 'index.html', {'form': form})
