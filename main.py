from fastapi import FastAPI
from router import assembly_router
from service_config import settings


def start_application():
   app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION) 
   app.include_router(assembly_router)
   return app


app = start_application()
