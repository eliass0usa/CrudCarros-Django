from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

EXEMPT_URLS = [
   reverse('login'),
    reverse('logout'),
]

class LoginRequiredMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
    
  def __call__(self, request):
    response = self.get_response(request)
    return response
  
  def process_view(self, request, view_func, view_args, view_kwargs):
    assert hasattr(request, 'user')
    if not request.user.is_authenticated:
        path = request.path_info.lstrip('/')
        if not any(url == path for url in EXEMPT_URLS):
          return redirect(settings.LOGIN_URL)