from django.shortcuts import render

from . import forms

def hello_world(request):
    return render(request, 'home.html')


def suggestion_form(request):
    form = forms.SuggestionForm(request)
    return render(request, 'suggestion_form.html', {'form': form})