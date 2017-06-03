from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

"""
class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)
    
class ListContactView(LoggedInMixin, generic.ListView):

    #model = Contact
    template_name = 'base.html'

    def get_queryset(self):
        return "Contact.objects.filter(owner=self.request.user)"
"""
class IndexView(generic.ListView):
    template_name = 'base.html'
#    context_object_name = 'latest_question_list'
    def get_queryset(self):
		return "Testcontent"


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
