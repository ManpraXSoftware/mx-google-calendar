from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
key_file_location = "/home/manprax/Desktop/firki2.0/google_calender/service_account.json"


class GoogleCalendarApi:
    def __init__(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=SCOPES)

        # Build the service object.

        self.service = build('calendar', 'v3', credentials=credentials)
        # return service

    def get_service(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=SCOPES)

        # Build the service object.

        service = build('calendar', 'v3', credentials=credentials)
        return service

    def create_calendar(self, calendar_name):
        print(
            "-------------------------creating new calendar-----------------------")
        created_calendar=None
        message=None
        body = {
            'summary': calendar_name,
            # 'timeZone': 'America/Los_Angeles'  #'timeZone': 'UTC'
        }
        try:
            created_calendar = self.service.calendars().insert(body=body).execute()
            message='calendar {} created'.format(calendar_name)
            # print(created_calendar['id'])
        except Exception as e:
            # print(e)
            message='Exception in create_calendar :{}'.format(e)
            print('Exception in create_calendar :{}'.format(e))

        return created_calendar,message

    def clear_calendar(self, calendar_id='primary'):
        '''
            clear events of the given calendar_id by default clears primary calendar
        '''
        print(
            "-------------------------clearing events of the given calendar-----------------------")
        service = self.get_service()
        response = self.service.calendars().clear('primary').execute()

        print(response)

    def delete_calendar(self, calendar_id='primary'):
        '''
            clear events of the given calendar_id by default clears primary calendar
        '''
        print(
            "-------------------------clearing events of the given calendar-----------------------")
        service = self.get_service()
        response = self.service.calendars().clear('primary').execute()

        print(response)

    def list_user_calendar(self):
        print("-------------------------Getting user's calendars-----------------------")
        service = self.get_service()
        page_token = None
        while True:
            calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(calendar_list_entry)
                print('----------------------------------------')
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break

    def get_calendar_by_name(self,calendar_name):
        service = self.get_service()
        # By default the page size can never be larger than 250 entries.
        # maxResults=100
        page_token = None
        calendar=None
        message='calendar {} not exists'.format(calendar_name)
        try:
            while True:
                calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
                filtered_list = list(filter(lambda x: x['summary'] == calendar_name, calendar_list['items']))
                if len(filtered_list):
                    calendar=filtered_list[0]
                    message="calendar {} already exists".format(calendar_name)
                    break
                elif not page_token:
                    break
                else:
                    page_token = calendar_list.get('nextPageToken')
        except Exception as e:
            message='Exception in get_calendar_by_name : {}'.format(e)
        return calendar,message



    def create_event(self, calendar_id, event_dic):
        calendar_id = "ul237tpd4st679bfufj8snkfh8@group.calendar.google.com"
        service = self.get_service()
        event = service.events().insert(calendarId=calendar_id, sendNotifications=True,
                                        conferenceDataVersion=1, body=event_dic).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        print('Event data: %s' % (event))
        return event['id']

    def create_acl_rule(self, calendar_id, user_email):
        # calendar_id = "8rp4khl5v5d9k9tnsq1mlglgv0@group.calendar.google.com"
        service = self.get_service()
        rule = {
            "role": "owner",
            "scope": {
                "type": "user",
                "value": user_email
            }
        }
        created_rule = service.acl().insert(calendarId=calendar_id,
                                            sendNotifications=True, body=rule).execute()
        print(created_rule['id'])

    def list_calendar_events(self, calendar_id):
        service = self.get_service()
        calendar_id = "ul237tpd4st679bfufj8snkfh8@group.calendar.google.com"

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('-----------------------Getting the upcoming 30 events------------------------------------')
        events_result = service.events().list(calendarId='primary',
                                              maxResults=30, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            if 'hangoutLink' in event:
                print(start, event['summary'], event['hangoutLink'])
            # elif 'summary' in event:
            #     print(start, event['summary'],event['htmlLink'])
            # else:
            #     print(start,event['htmlLink'])

    def update_event(self, calendar_id, event_id, start, end, description):
        service = self.get_service()
        try:
            event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
        except HttpError as e:
            if e.resp.status == 404:
                return self.create_event(calendar_id, start, end, description)
        event["start"] = {'dateTime': start}
        event["end"] = {'dateTime': end}
        event["summary"] = description
        event["description"] = description
        updated_event = service.events().update(
            calendarId=calendar_id, eventId=event['id'], body=event).execute()
        return updated_event["id"]


if __name__ == '__main__':
    event = {
        'summary': 'random event from code',
        'sendUpdates': "all",
        # 'location': 'Any location',
        'description': 'random event from code',
        'start': {
            'dateTime': '2020-04-27T11:45:00.603111+05:30',
        },
        'end': {
            'dateTime': '2020-04-27T11:50:00.603111+05:30',
        },
        # 'attendees': [
        #     {'email': 'kritika2014arora@gmail.com'},
        #     {'email': 'mishramail10@gmail.com'},
        #     {'email': 'praveenmishra1493@gmail.com'},
        # ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
        "conferenceData": {
            "createRequest": {
                "requestId": "12345678910"
            }
        }
    }
    # m = GoogleCalendarApi()

    # # # create event
    # # m.create_event(calendar_id='primary', event_dic=event)

    # # # list primary calendar events
    # # m.list_calendar_events(calendar_id='primary')

    # # created_calendar_id = m.create_calendar(calendar_name="Anurag calendar 4")
    # # m.create_acl_rule(calendar_id=created_calendar_id,
    # #   user_email = "kritika2015arora@gmail.com")
    # m.list_user_calendar()
    # # m.clear_calendar(self, calendar_id)
