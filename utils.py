import secrets
from fastapi import Security
from fastapi.security import  HTTPBasic, HTTPBasicCredentials
from service_config.settings import settings




class AuthHandler():
   basic_security = HTTPBasic()
   def decode_basic_creds(self, payload):
       username = settings.USERNAME
       password = settings.PASSWORD
       try:
           current_username = payload.username
           current_password = payload.password
           is_correct_username = secrets.compare_digest(
           current_username, username
           )
           is_correct_password = secrets.compare_digest(
               current_password, password
           )
           if(is_correct_username and is_correct_password):
               return True
           else:
               return False
       except Exception as excp:
           print("caught exception while decoding basic auth",excp)

   def basic_auth_access_wrapper(self, auth: HTTPBasicCredentials = Security(basic_security)):
       return self.decode_basic_creds(auth)
  
