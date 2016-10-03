from django.shortcuts import render, render_to_response

def home(request):
    return render_to_response('home_family/home.html')
