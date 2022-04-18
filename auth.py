from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)

credentials = flow.run_console()

import pickle

pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()

result['items'][0]

{'kind': 'calendar#calendarListEntry',
 'etag': '"1557422762384000"',
 'id': 'kashanahmad036@gmail.com ',
 'summary': 'kashanahmad036@gmail.com',
 'timeZone': 'Asia/Kolkata',
 'colorId': '14',
 'backgroundColor': '#9fe1e7',
 'foregroundColor': '#000000',
 'selected': True,
 'accessRole': 'owner',
 'defaultReminders': [{'method': 'popup', 'minutes': 30}],
 'notificationSettings': {'notifications': [{'type': 'eventCreation',
    'method': 'email'},
   {'type': 'eventChange', 'method': 'email'},
   {'type': 'eventCancellation', 'method': 'email'},
   {'type': 'eventResponse', 'method': 'email'}]},
 'primary': True,
 'conferenceProperties': {'allowedConferenceSolutionTypes': ['eventHangout']}}

calendar_id = result['items'][0]['id']

result = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()

result['items'][0]

{'kind': 'calendar#event',
 'etag': '"3114856233680000"',
 'id': '0slqq110a9171scjmrfojjquse',
 'status': 'confirmed',
 'htmlLink': 'https://www.google.com/calendar/event?eid=MHNscXExMTBhOTE3MXNjam1yZm9qanF1c2UgaW5kaWFucHl0aG9uaXN0YUBt&ctz=Asia/Kolkata',
 'created': '2019-05-09T18:55:16.000Z',
 'updated': '2019-05-09T18:55:16.840Z',
 'summary': 'Meeting',
 'creator': {'email': 'indianpythonista@gmail.com', 'self': True},
 'organizer': {'email': 'indianpythonista@gmail.com', 'self': True},
 'start': {'dateTime': '2019-05-05T02:30:00+05:30'},
 'end': {'dateTime': '2019-05-05T03:30:00+05:30'},
 'iCalUID': '0slqq110a9171scjmrfojjquse@google.com',
 'sequence': 0,
 'extendedProperties': {'private': {'everyoneDeclinedDismissed': '-1'}},'reminders': {'useDefault': True}}
from datetime import datetime, timedelta

start_time = datetime(2019, 5, 12, 19, 30, 0)
end_time = start_time + timedelta(hours=4)
timezone = 'Asia/Kolkata'

event = {
  'summary': 'IPL Final 2019',
  'location': 'Hyderabad',
  'description': 'MI vs TBD',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}
service.events().insert(calendarId=calendar_id, body=event).execute()

{'kind': 'calendar#event',
 'etag': '"3114964833447000"',
 'id': 'advb4ftvjbivf7jaru9g1dbp5s',
 'status': 'confirmed',
 'htmlLink': 'https://www.google.com/calendar/event?eid=YWR2YjRmdHZqYml2ZjdqYXJ1OWcxZGJwNXMgaW5kaWFucHl0aG9uaXN0YUBt',
 'created': '2019-05-10T10:00:16.000Z',
 'updated': '2019-05-10T10:00:16.759Z',
 'summary': 'IPL Final 2019',
 'description': 'MI vs TBD',
 'location': 'Hyderabad',
 'creator': {'email': 'indianpythonista@gmail.com', 'self': True},
 'organizer': {'email': 'indianpythonista@gmail.com', 'self': True},
 'start': {'dateTime': '2019-05-12T19:30:00+05:30',
  'timeZone': 'Asia/Kolkata'},
 'end': {'dateTime': '2019-05-12T23:30:00+05:30', 'timeZone': 'Asia/Kolkata'},
 'iCalUID': 'advb4ftvjbivf7jaru9g1dbp5s@google.com',
 'sequence': 0,
 'reminders': {'useDefault': False,
  'overrides': [{'method': 'email', 'minutes': 1440},
   {'method': 'popup', 'minutes': 10}]}}


