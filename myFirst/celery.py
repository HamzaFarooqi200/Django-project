from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Set default Django settings module for 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basicSetup.settings")

app = Celery("model_task")

# Load settings from Django settings file.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
