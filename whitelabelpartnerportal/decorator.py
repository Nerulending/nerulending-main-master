from functools import wraps
from django.http import HttpResponseRedirect
from dynamic.models import *
from yourplan.models import *

def partner_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    try:
        user = Profile.objects.get(user=request.user)
        if user.is_partner:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')            
    except Exception:
        return function(request, *args, **kwargs)

  return wrap