from __future__ import absolute_import, unicode_literals


from celery import Celery


from service_config.celery_config import celery_settings




def create_celery():
   celery_app = Celery('Assembly', include=[
   'schedule_tasks'
   ])
   celery_app.config_from_object(celery_settings, namespace='CELERY')
   celery_app.conf.update(accept_content=['json', 'pickle'])
   celery_app.conf.update(result_backend='rpc://')
   celery_app.conf.update(timezone='Asia/Kolkata')
   celery_app.conf.update(broker_connection_retry_on_startup=True)


   # Load task modules across the project.
   celery_app.autodiscover_tasks()


   return celery_app




celery_app = create_celery()
