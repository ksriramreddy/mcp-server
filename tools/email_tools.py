from google_auth.auth import GoogleAuthentication
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from googleapiclient.discovery import build
from email.message import EmailMessage
import mimetypes
import os
import base64
from bs4 import BeautifulSoup
from mimetypes import guess_type 


class EmailTools(GoogleAuthentication):
    def read_emails(self, n : int):
        """
        Reads email
        n : number of emails
        Return : Dict that contains Email content
        """
        service = build("gmail", "v1", credentials=self.creds)
        results = service.users().messages().list(userId="me", maxResults=n).execute()
        messages = results.get("messages", [])
        
        emails = []

        for msg in messages:
            result = service.users().messages().get(userId="me", id=msg['id'], format='full').execute()
            payload = result.get("payload", {})
            headers = payload.get("headers", [])
            parts = payload.get("parts", [])
            message_id = result.get("id", "")

            # Extract sender and subject
            sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown")
            subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")

            # Decode body
            body = self._get_email_body(payload)

            emails.append({
                'subject': subject,
                'sender': sender,
                'body': body,
                'labelIds': result.get('labelIds', []),
                'message_id': message_id,
            })  
        
        def clean_email_data(email):
            subject = email.get('subject', '')
            sender = email.get('sender', '')
            raw_body = email.get('body', '')
            label = email.get('label', '')
            message_id = email.get('message_id', '')

            # Clean HTML body
            soup = BeautifulSoup(raw_body, 'html.parser')
            clean_text = soup.get_text(separator=' ', strip=True)

            return {
                'subject': subject,
                'sender': sender,
                'body': clean_text,
                'message_id': message_id,
                'label': label
            }
                    
        cleaned_emails = [clean_email_data(email) for email in emails] 
     
        return {'emails': cleaned_emails}
        
    def _get_email_body(self, payload):
        
        """Extract and decode the email body from the payload."""
        body_data = ""

        if "parts" in payload:
            for part in payload["parts"]:
                mime_type = part.get("mimeType", "")
                if mime_type in ["text/html", "text/plain"]:
                    body_data = part.get("body", {}).get("data", "")
                    break
        else:
            body_data = payload.get("body", {}).get("data", "")

        if body_data:
            try:
                return base64.urlsafe_b64decode(body_data).decode("utf-8")
            except Exception as e:
                return f"(Decode error: {e})"

        return "(No content)"
                
    def send_email(self, to: str, subject: str, body: str):
        """
        Send email with PDF attachment via Gmail API.
        """
        try:
            service = build("gmail", "v1", credentials=self.creds)

            resume_path = os.path.abspath("ksriramreddy.pdf")  # Ensure correct absolute path
            if not os.path.exists(resume_path):
                return {"error": "Resume file not found!"}

            # Detect MIME type of the resume
            mime_type, _ = guess_type(resume_path)
            if not mime_type:
                mime_type = "application/pdf"  # fallback
            maintype, subtype = mime_type.split("/")

            # Create the email message
            message = EmailMessage()
            message["To"] = to
            message["From"] = "me"
            message["Subject"] = subject
            message.set_content(body)  # plain text or html

            # Read and attach the resume
            # with open(resume_path, "rb") as f:
            #     file_data = f.read()
            #     message.add_attachment(file_data,
            #                         maintype=maintype,
            #                         subtype=subtype,
            #                         filename="resume.pdf")

            # Encode and send the message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            send_result = service.users().messages().send(userId="me", body={"raw": encoded_message}).execute()

            return {
                "status": "Email with resume sent successfully",
                "message_id": send_result.get("id")
            }

        except Exception as e:
            return {"error": str(e)}
                
            
print(EmailTools().send_email(to="ramsri123123123@gmail.com",body="This is a text mail",subject="Testing"))

resume_path = os.path.abspath("ksriramreddy.pdf")
print("Resume path:", resume_path)