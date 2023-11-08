from service_config.celery import celery_app
from operation import generate_report

app = celery_app

@app.task
def process_report():
    report_status = generate_report()
    print(report_status)