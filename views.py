from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from calendar_apis.utils import GoogleCalendarApi
client_email = "google-calendar-app@striped-antler-275611.iam.gserviceaccount.com"
private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMu1Z+iRGafcEu\nd+tTqMR8QeWLMVVorSNOvK9rhIlRrPkvVcHtH8L0Kt3+ls1zKzlQ8W7xzxqF6WrM\nPgetVzK77p+GicZOrUiWRycmt0LZHKqsjispLeQ/6dzPw8ikfU/X7KO5zRwWBWVh\nmzoR9HHej7Dz+YlZL/RtQhC7a75+gMdVSm/AcKpVZuLZHb9u//xWl16rFG5WhLV7\nL67/rRW6JcC2piX4UaF+dVyC1Yw1+8BXYfJemZoM2mTIeV8cakfNshQaQTp0aoQh\nyiCSSR5zEy40T9WM5PArZmZI0f7LBSq0Ub47+8kGZ5x4vyzlxCoAVjAT2CsxYVZt\nyI+L+P2lAgMBAAECggEABVe9IsLAuqi7jTV4BGs8CNFT4dkRAaS7Wn606HWVBTH6\n0V/95RQ7ErRgcvD4m6mwhxwKJs5PrxMtNYEMv4vy9pG3Vy+qjtPBENWr08XI7opi\nAzsD8gX4X8p2KSVmaTuTyhrv7/Lt1eYM/zZujFPJyHtcLIw4HhmuY3Z1jno+6OVU\nyotAqgd1wC4NcKvJUl3Gb0ZpHee3sMNuNpCcHKVr03z8cWLvSurOwgKsF2R2D6eW\nPhqgC6/rogdqio+VnUitHAeVTfyyMOFibf74nPBwcfhNJmAJiSl/DGXL3hSkckUa\n2PkQ0bykJGRloYf5iS1GsWmpZ63M8eL2AFPOFX9ZawKBgQDtpp9vBT19u6017XbL\n/muZoqk/KCdpx2Z2iZX0KqQaPGPSih73aZdXNyybK6u8W2LLYUB1dDCPmgYWjSP2\nTKtFgT+CVjCbrEec4pz872Gh4/Rwq0FS1z9yquYWHcRnIb2r8/MfTbF7AxCxnm+2\nwE8kcqFspqT3oGw7Pnpzb481UwKBgQDcigpoI1UmoesU/4DRL3DpVJNoYKfd4sd3\nmY+cdy8aqX/Hw7c6BlbJklgMTiPO+RZ88xlvNo76ZNUPjtI8qDtrCncxsVfBwBaS\nP/lg1gN10dG4tSI2j0PUh8LXslq+p9IhidiGBU0sL2plWGo123vYleQxx3CygTzJ\nfqe2+K7qJwKBgDmC/UpsxjjLVluaoAk2BOwlRTgXi5I5wz4khbmVKCmBO9cTvfK6\nBvoATDcxFlp68yms22CRQb8+0wJaHb3ZSAmGAcyU9yZ1Rs9cuAkuFT6MX/d0OlbF\n6IDjgtMPWRxsOe6HFusYbj8KutuBMB/V4lE7vH0CxyF2HTspH5EYClwpAoGAJ15Q\n+0QLaEkRQP9XTIBOhKh/Y+uVK8vW1afI9iJkezr0v4FVjPsitPr10sSEKedXN1ji\nGnM/1Lz5N7zEFOXnLXWBz5Ib209h+BuJddreZULeUD2tbNXoQuE1S/HftxcYMLp9\nt3bszs1sDclZtGGI2yHuyWAT4xmk80czwzrjZpMCgYEAlccYS/PH0sNiuH4AxIHR\n8rOBpcyaowVXXXtwpN85m7EQQsf3Kfueh/lJ/x81DDufO43oleaz1fNumYN5CBCI\niz593PJFpvqTk/Fr0djlSXdQu1aDztxD7IbX/bdkfpbzHL49FSYIKyRMPN5p37Yw\nwOExACydRWlXvAGwUvOqmgU=\n-----END PRIVATE KEY-----\n"
private_key_id = "a90a38ab28216454259c3dd862f8e4eefc0787db"
client_id = "109937249692533555705"

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
    response={'event':None,'status':False,'message':None}
    try:
        if calendarId and eventId:
            calendarapi_obj = GoogleCalendarApi(
                client_email, private_key, private_key_id, client_id)
            event,message,found=calendarapi_obj.get_event(calendarId,eventId)
            response['event'] = event
            response['message'] = message
            response['found'] = found
            status_code=status.HTTP_200_OK
        else:
            response['message'] = 'calendarId and eventId are required'
            status_code=status.HTTP_400_BAD_REQUEST

    except Exception as e:
        response['message'] = 'exception in api{}'.format(e)
        status_code=status.HTTP_400_BAD_REQUEST
    return Response(response,status=status_code)


@api_view(["POST"])
def create_event(request):
    calendarId=request.query_params.get('calendarId')
    event_payload=request.data
    if not calendarId:
        response={
            'message':"calendarId is required",
            'created':False,
            'event':None
        }
        status_code=status.HTTP_400_BAD_REQUEST
    elif calendarId and not event_payload:
        response={
            'message':"start and end  event times are required",
            'created':False,
            'event':None
        }
        status_code=status.HTTP_400_BAD_REQUEST
    else:
        obj = GoogleCalendarApi(
                client_email, private_key, private_key_id, client_id)
        event,message,created=obj.create_event(calendarId,event_payload)
        response={
                'message':message,
                'created':created,
                'event':event
            }
    if not created:
        status_code=status.HTTP_400_BAD_REQUEST
    else:
        status_code=status.HTTP_200_OK

    return Response(response,status=status_code)