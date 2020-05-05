from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import GoogleCalendarApi

client_email = settings.GOOGLE_CALENDAR_API['client_email']
private_key = settings.GOOGLE_CALENDAR_API['private_key']
private_key_id = settings.GOOGLE_CALENDAR_API['private_key_id']
client_id = settings.GOOGLE_CALENDAR_API['client_id']

# Create your views here.
@api_view(["POST"])
def create_calendar(request):
    payload = request.data
    calendar_name = request.data.get("calendar_name", '')
    response = {
        'id': None,
        'name': None,
        'message': 'calendar {} not created'.format(calendar_name),
        'status': False
    }
    try:
        if calendar_name:
            obj = GoogleCalendarApi(
                client_email, private_key, private_key_id, client_id)
            # if calendar already present
            calendar, message = obj.get_calendar_by_name(
                calendar_name)  # if duplicacy returns calendar else None
            # create new calendar
            if not calendar:
                calendar, message = obj.create_calendar(calendar_name)
                response['message'] = message
                # exception in creating new calendar
                if not calendar:
                    response['status'] = False
                else:
                    response['id'] = calendar['id']
                    response['name'] = calendar['summary']
                    response['status'] = True
            else:
                response['id'] = calendar['id']
                response['name'] = calendar['summary']
                response['message'] = message
            return Response(response)
        else:
            response['message'] = 'calendar_name not provided'

            return Response(response)
    except Exception as e:
        response['message'] = 'exception in api{}'.format(e)
        return Response(response)


# Create your views here.
@api_view(["GET"])
def get_event(request):
    calendarId = request.GET.get("calendarId")
    eventId = request.GET.get("eventId")
    response={'status':False,'message':None,'event':None}
    try:
        if calendarId and eventId:
            calendarapi_obj = GoogleCalendarApi(
                client_email, private_key, private_key_id, client_id)
            response['event'],response['message'],response['status']=calendarapi_obj.get_event(calendarId,eventId)
        else:
            response['message'] = 'calendarId and eventId are required'
    except Exception as e:
        response['message'] = 'exception in api{}'.format(e)

    if not response['status']:
        status_code=status.HTTP_400_BAD_REQUEST
    else:
        status_code=status.HTTP_200_OK
    return Response(response,status=status_code)


@api_view(["POST"])
def create_event(request):
    calendarId=request.query_params.get('calendarId')
    event_payload=request.data
    response={'status':False,'message':None,'event':None}
    if not calendarId or not event_payload:
        response['message']="calendarId and  event details are required"
        response['status']=False
        response['event']=None
    else:
        obj = GoogleCalendarApi(
                client_email, private_key, private_key_id, client_id)
        response['event'],response['message'],response['status']=obj.create_event(calendarId,event_payload)
    if not response['status']:
        status_code=status.HTTP_400_BAD_REQUEST
    else:
        status_code=status.HTTP_200_OK
    return Response(response,status=status_code)

@api_view(["GET"])
def get_calendar_events(request):
    calendarId = request.GET.get("calendarId")
    timeMax = request.GET.get("timeMax")
    timeMin = request.GET.get("timeMin")
    nextPageToken= request.GET.get("nextPageToken")
    text_search = request.GET.get("text_search")
    response={'status':False,'message':None,'events':None,'nextPageToken':None}
    try:
        if not calendarId:
            response['message']="calendarId is required",
            response['events']=None,
            response['nextPageToken']=None
        else:
            obj = GoogleCalendarApi(
                client_email, private_key, private_key_id, client_id)
            response['events'],response['nextPageToken'],response['message']=obj.get_calendar_events(calendarId,timeMax,timeMin,nextPageToken)
    except Exception as e:
        response['message'] = 'exception in api{}'.format(e)
    if not response['status']:
        status_code=status.HTTP_400_BAD_REQUEST
    else:
        status_code=status.HTTP_200_OK
    return Response(response,status=status_code)