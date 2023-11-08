from kombu import Queue, Exchange
from service_config import settings

class BaseConfigSettings(object):
   CELERY_BROKER_URL: str = settings.CELERY_BROKER_URL
   CELERY_TASK_QUEUES = (
       Queue(
           name="report",
           exchange=Exchange("default", type="direct"),
           routing_key="report"
       )
   )
   CELERY_TASK_CREATE_MISSING_QUEUES = True

def get_settings():
   return BaseConfigSettings()

celery_settings = get_settings()