import logging
from django.test import TestCase, RequestFactory, Client
from django.utils import timezone
from .models import RateLimit, CustomUser
from .middlewares.middleware import IpLogMiddleware
from django.http import HttpResponseForbidden
from django.urls import reverse


class IpLogMiddlewareTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = IpLogMiddleware(get_response=lambda req: HttpResponseForbidden())

    def test_log_message(self):
        request = self.factory.get('/')
        response = self.middleware(request)
        self.assertEqual(response.status_code, 403)

        # Check if the log message was written to the file
        with open('requests.txt', 'r') as f:
            log_message = f.read()
            self.assertIn('the ip address is:', log_message)
            self.assertIn('and at time:', log_message)

    def test_log_level(self):
        request = self.factory.get('/')
        response = self.middleware(request)
        self.assertEqual(response.status_code, 403) 

        logger = logging.getLogger('django')
        self.assertEqual(logger.level, logging.INFO)

    

class AccessControlTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='testuser78@gmail.com', password='password')

    # def test_authenticated_access(self):
    #     self.client.login(email='testuser78@gmail.com', password='password')
    #     response = self.client.get(reverse('thanks_view'))
    #     self.assertEqual(response.status_code, 200)

    def test_unauthenticated_access(self):
        response = self.client.get(reverse('thanks_view'))
        print(f"response is: {response}")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('thanks_view'))



class RateLimitMiddlewareTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='testuser78@gmail.com', password='password')
        self.client.login(email='testuser78@gmail.com', password='password')

    def create_rate_limit(self, user, req_count=0, login_time=None):
        if login_time is None:
            login_time = timezone.now() - timezone.timedelta(minutes=1)
        RateLimit.objects.create(user=user, req_count=req_count, login_time=login_time)
    
    def test_rate_limit_enforcement(self):
        self.create_rate_limit(self.user)
    
        for i in range(5):
            response = self.client.get('/model_task/login/', follow=True)
            self.assertEqual(response.status_code, 200)
            RateLimit.objects.filter(user=self.user).update(req_count=i+1)
        
        RateLimit.objects.filter(user=self.user).update(login_time=timezone.now() - timezone.timedelta(minutes=2), req_count=0)
        
        response = self.client.get('/model_task/login/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_excluded_paths(self):
        response = self.client.get('/admin/', follow=True)
        self.assertEqual(response.status_code, 200)