

from fastapi import APIRouter, Depends
from utils import AuthHandler
from service_config.settings import settings
from service import trigger_report, get_report_in_csv


auth_handler = AuthHandler()


assembly_router = APIRouter(
   prefix="/assembly/v1",
   tags=["Report"]
)


@assembly_router.get("/report")
async def get_report(report_id:str, is_allowed = Depends(auth_handler.basic_auth_access_wrapper)):
   return await get_report_in_csv(is_allowed)

@assembly_router.post("/trigger")
async def trigger(is_allowed = Depends(auth_handler.basic_auth_access_wrapper)):
   return await trigger_report(is_allowed)