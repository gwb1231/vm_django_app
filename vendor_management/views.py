from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Vendor
from django.views import generic

# Create your views here.
def index(request):
    latest_vendor_list = Vendor.objects.order_by()

def vendor_list(request, id):
    return HttpResponse('You are looking at vendor %s.' % id)

class DetailView(generic.DetailView):
    model = Vendor
    template_name = 'vendor_management/detail.html'


class ResultsView(generic.DetailView):
    model = Vendor
    template_name = 'vendor_management/results.html'