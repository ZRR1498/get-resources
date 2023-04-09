import os
import sys
from datetime import timedelta

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: ['main_app'])

app.conf.beat_schedule = {
    "process_call_all_services_task": {
        "task": "main_app.tasks.process_call_all_services",
        "schedule": timedelta(seconds=10),
    },
}
