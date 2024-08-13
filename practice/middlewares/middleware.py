from django.utils.deprecation import MiddlewareMixin

class SampleMiddleware(MiddlewareMixin):
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):

    # Retrieving the response
    response = self.get_response(request)
    return response