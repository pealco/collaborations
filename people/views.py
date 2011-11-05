from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from people.models import *

from django.utils import simplejson

def people_json(request):
    people = Person.objects.filter(is_active=True, is_alum=False).order_by('last_name')
    nodes = dict([(person.full_name(),{}) for person in people])    
    edges = dict([(person.full_name(), dict([(collab.full_name(), {}) for collab in person.collaborators.all()])) for person in people])
    js = {"nodes": nodes, "edges": edges}
    js = simplejson.dumps(js)
    
    return HttpResponse(js)
    

def main_page(request):
    people = Person.objects.filter(is_active=True, is_alum=False).order_by('last_name')

    variables = Context({
        'people': people,
    })
    return render_to_response('main.html', variables)