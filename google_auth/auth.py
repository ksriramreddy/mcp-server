# from auth import GoogleAuthentication
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/calendar"
]


class GoogleAuthentication:
    def __init__(self):
        self.path = "token.json"    
        self.creds = self.authenticate_user()
    def authenticate_user(self):
        creds = None
        if os.path.exists(path=self.path):
            creds = Credentials.from_authorized_user_file(self.path,SCOPES)
            
        if not creds or creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credential.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open(self.path, "w") as token_file:
                token_file.write(creds.to_json())
            
        return creds
    
    
# print(GoogleAuthentication().authenticate_user())
