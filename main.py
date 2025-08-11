from typing import Any
import httpx
from fastmcp import FastMCP
from tools.email_tools import EmailTools
from tools.calendar_tool import CalendarMCP
# Initialize FastMCP server
mcp = FastMCP("emailMCP")

email_tool = EmailTools()
calendar_tool = CalendarMCP()

@mcp.tool() 
def read_emails(n_emails : int):
    """
    Reads email based on given n emails
    Args:
        n_emails : Number of emails to read
    Return:
        Dict : Contains Email content
    """
    return email_tool.read_emails(n=n_emails)

@mcp.tool()
def write_email(to : str , subject : str, body : str):
    """
    This function will sends email to passes email id
        args:
            to(str) : Recipents email
            subject(str) : Subject or title of purpos
            body(str) : Email body content (generated based on requirement)
        Return: 
            dict : Return a Success or error message 
    """
    return email_tool.send_email(to=to,subject=subject,body=body)

@mcp.tool()
def create_meeting(summary: str, description: str, start_time: str, end_time: str, timezone: str = "UTC"):
    """
    Creates a new meeting/event in Google Calendar.

    Args:
        summary (str): Title of the meeting/event.
        description (str): Detailed description or agenda of the meeting.
        start_time (str): Start time of the event in RFC3339 format (e.g., "2025-08-11T10:00:00+05:30").
        end_time (str): End time of the event in RFC3339 format.
        timezone (str): Timezone identifier (default: "UTC").

    Returns:
        dict: Contains status and event details (event_id, html_link).
    """
    return calendar_tool.create_event(
        summary=summary,
        description=description,
        start_time=start_time,
        end_time=end_time,
        timezone=timezone
    )


@mcp.tool()
def update_meeting(event_id: str, summary: str = None, description: str = None,
                   start_time: str = None, end_time: str = None, timezone: str = None):
    """
    Updates an existing meeting/event in Google Calendar.

    Args:
        event_id (str): The unique Google Calendar event ID.
        summary (str, optional): New title for the meeting/event.
        description (str, optional): New description or agenda.
        start_time (str, optional): New start time in RFC3339 format.
        end_time (str, optional): New end time in RFC3339 format.
        timezone (str, optional): Timezone identifier.

    Returns:
        dict: Contains status and updated event details.
    """
    return calendar_tool.update_event(
        event_id=event_id,
        summary=summary,
        description=description,
        start_time=start_time,
        end_time=end_time,
        timezone=timezone
    )


@mcp.tool()
def delete_meeting(event_id: str):
    """
    Deletes an existing meeting/event from Google Calendar.

    Args:
        event_id (str): The unique Google Calendar event ID.

    Returns:
        dict: Contains status and confirmation message.
    """
    return calendar_tool.delete_event(event_id=event_id)

@mcp.tool()
def get_meets(date_str : str):
    """
    Fetch all events for a specific date.
    Args:
        date_str (str): Date in 'YYYY-MM-DD' format
    Returns:
        dict: List of events with details
    """
    return calendar_tool.get_events_for_date(date_str=date_str)

if __name__ == "__main__":
    # Initialize and run the server   
    mcp.run(transport='stdio')