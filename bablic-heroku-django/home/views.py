# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext


def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))
