from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from  google_auth.auth import GoogleAuthentication
from datetime import datetime, timedelta

class CalendarMCP(GoogleAuthentication):
    def __init__(self):
        super().__init__()
        self.service = build("calendar", "v3", credentials=self.creds)

    def create_event(self, summary, description, start_time, end_time, timezone="UTC"):
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_time,
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time,
                'timeZone': timezone,
            }
        }
        created_event = self.service.events().insert(calendarId='primary', body=event).execute()
        return {"status": "success", "eventId": created_event.get("id")}

    def update_event(self, event_id, summary=None, description=None, start_time=None, end_time=None):
        event = self.service.events().get(calendarId='primary', eventId=event_id).execute()
        
        if summary:
            event['summary'] = summary
        if description:
            event['description'] = description
        if start_time:
            event['start']['dateTime'] = start_time
        if end_time:
            event['end']['dateTime'] = end_time
        
        updated_event = self.service.events().update(calendarId='primary', eventId=event_id, body=event).execute()
        return {"status": "updated", "eventId": updated_event.get("id")}

    def delete_event(self, event_id):
        self.service.events().delete(calendarId='primary', eventId=event_id).execute()
        return {"status": "deleted", "eventId": event_id}
    
    
    def get_events_for_date(self, date_str):
        """
        Fetch all events for a specific date.
        Args:
            date_str (str): Date in 'YYYY-MM-DD' format
        Returns:
            dict: List of events with details
        """
        try:
            # Parse the given date
            start_of_day = datetime.strptime(date_str, "%Y-%m-%d")
            end_of_day = start_of_day + timedelta(days=1)

            # Convert to RFC3339 format for Google Calendar API
            start_iso = start_of_day.isoformat() + "Z"
            end_iso = end_of_day.isoformat() + "Z"

            events_result = self.service.events().list(
                calendarId='primary',
                timeMin=start_iso,
                timeMax=end_iso,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            events = events_result.get('items', [])
            event_list = []

            for event in events:
                event_list.append({
                    "id": event.get("id"),
                    "summary": event.get("summary"),
                    "description": event.get("description", ""),
                    "start": event["start"].get("dateTime", event["start"].get("date")),
                    "end": event["end"].get("dateTime", event["end"].get("date"))
                })

            return {"status": "success", "events": event_list}

        except Exception as e:
            return {"status": "error", "message": str(e)}