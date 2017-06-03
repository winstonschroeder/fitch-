from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'index.html'
#    context_object_name = 'latest_question_list'
    def get_queryset(self):
		return "Testcontent"


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
