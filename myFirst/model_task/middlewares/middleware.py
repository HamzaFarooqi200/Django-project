import logging
from django.utils import timezone
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from ..models import RateLimit, CustomUser
from django.contrib.auth import login

logger = logging.getLogger('django')
class IpLogMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
      self.get_response = get_response

    def __call__(self, request):

    # Retrieving the response
      ip_address = request.META.get("REMOTE_ADDR")
      timestamp = timezone.now()
      logger.info(f'the ip address is: {ip_address} and and at time: {timestamp}')
      response = self.get_response(request)

      print(f"Custom middl ware: {request.path}")
      return response
    
# class LimitMiddleware(MiddlewareMixin):
#     RATE_LIMIT = 5
#     def __init__(self, get_response):
#       self.get_response = get_response

#     def __call__(self, request):
#       curr_user = User.objects.filter(email="bilal@gmail.com").get()
#       login(request, curr_user)
#       print(f"Custom rate limit middleware: {request.path}")
#       print("User", request.user)
#       try:
#         curr = Rate_limit.objects.filter(user=request.user).get()
#       except:
#          curr = Rate_limit.objects.create(request.user)
      
#       return self.handle_limit(request, curr)
    
#     def handle_limit(self, req, user):
#       now = timezone.now()
#       limit = self.get_max_requests(user.user.role)
#       time_window = timezone.timedelta(minutes=1)

#       if (now - user.login_time) > time_window:
#         user.req_count  = 1
#         user.login_time = now
#         user.save()

#       else:
#         user.req_count += 1
#         print("LIMIT", user.req_count)
#         if user.req_count > limit:
#             return HttpResponse("Rate limit exceed!")
#         user.save()

#       response = self.get_response(req)
#       return response

#     def get_max_requests(self, role):
#         if role == 'g':
#             return 10  # GOLD users
#         elif role == 's':
#             return 5   # SILVER users
#         elif role == 'b':
#             return 2   # BRONZE users
#         elif role == 'u':
#             return 1   # UNAUTHENTICATED users
#         else:
#             return 1   # Default rate limit if role is unknown

#     def handle_default_rate_limit(self, request):
#         # Use default rate limit based on IP address for unauthenticated users
#         user_key = request.META.get('REMOTE_ADDR')
#         cache_key = f"rate_limit_{user_key}"
        
#         response = self.get_response(request)
#         return response     
