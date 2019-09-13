from __future__ import print_function
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None

#Connect to the calendar
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()

    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

CAL = build('calendar', 'v3', credentials=creds)

class HomeScreen(Screen):
    def nextScreen(self):
        self.manager.current = "input"


#Input screen where we input the information about the class as well as the assignment and due date
class InputScreen(Screen):
    #Create the calendar event
    def addToCalendar(self):
        theYear = self.theYear.text
        theMonth = self.theMonth.text
        theDay = self.theDay.text
        EVENT = {
            "summary": self.className.text + " Assignment Due",
            "description": self.assignment.text,
            "start": {"dateTime": theYear + "-" + theMonth + "-" + theDay + "T23:00:00-05:00",
                      "timeZone": "America/Chicago",
            },
            "end": {"dateTime": theYear + "-" + theMonth + "-" + theDay + "T23:00:00-05:00",
                      "timeZone": "America/Chicago",
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "email", "minutes": 60*10},
                    {"method": "popup", "minutes": 60*10},
                ],
            },
        }
        e = CAL.events().insert(calendarId='primary', sendNotifications=True, body=EVENT).execute()
        self.assignment.text = ""
        self.className.text = ""

class Stages(ScreenManager):
    pass

test = Builder.load_file("hws.kv")

class HWS(App):
    def build(self):
        return test

if __name__ == "__main__":
    HWS().run()
