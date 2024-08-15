import logging

from django.http import HttpResponseForbidden
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from ..models import RateLimit

logger = logging.getLogger("django")


class IpLogMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        ip_address = request.META.get("REMOTE_ADDR")
        current_time = timezone.now()
        message = f"the ip address is: {ip_address} and and at time: {current_time}"
        logging.getLogger("django").info(message)
        return response


class LimitMiddleware(MiddlewareMixin):
    EXCLUDED_PATHS = ["admin", "signup"]
    RATE_LIMIT = 5

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(f"Custom rate limit middleware: {request.path}")
        if request.user.is_authenticated:
            curr = RateLimit.objects.filter(user=request.user).first()
            if curr:
                response = self.handle_limit(request, curr)
                if response:
                    return response
            return self.get_response(request)
        return self.get_response(request)

    def handle_limit(self, req, user):
        now = timezone.now()
        limit = self.get_max_requests(user.user.role)
        time_window = timezone.timedelta(minutes=1)

        if not any(excluded_path in req.path for excluded_path in self.EXCLUDED_PATHS):
            if (now - user.login_time) > time_window:
                # print(f'-------nw')
                user.req_count = 1
                user.login_time = now
                user.save()

            else:
                # print(f'-------else Limit is {limit}')
                if user.req_count >= limit:
                    # print("LIMIT is done!!!")
                    return HttpResponseForbidden("Rate limit exceed!")
                user.req_count += 1
                # print("LIMIT", user.req_count)
                user.save()

    def get_max_requests(self, role):
        if role == "g":
            return 10  # GOLD users
        elif role == "s":
            return 5  # SILVER users
        elif role == "b":
            return 2  # BRONZE users
        elif role == "u":
            return 20  # UNAUTHENTICATED users
        else:
            return 20  # Default rate limit if role is unknown
