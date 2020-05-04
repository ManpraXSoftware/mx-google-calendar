from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from calendar_apis.utils import GoogleCalendarApi

# Create your views here.
@api_view(["POST"])
def create_calendar(request):
    payload = request.data
    calendar_name=request.data.get("calendar_name",'')
    response={
        'id': None,
        'name': None,
        'message':'calendar {} not created'.format(calendar_name),
        'status':False
    }
    try:
        if calendar_name:
            obj=GoogleCalendarApi()
            # if calendar already present
            calendar,message=obj.get_calendar_by_name(calendar_name)  # if duplicacy returns calendar else None
            # create new calendar
            if not calendar:
                calendar,message=obj.create_calendar(calendar_name)
                response['message']=message
                # exception in creating new calendar
                if not calendar:
                    response['status']=False
                else:
                    response['id']=calendar['id']
                    response['name']=calendar['summary']
                    response['status']=True
            else:
                response['id']=calendar['id']
                response['name']=calendar['summary']
                response['message']=message
            return Response(response)
        else:
            response['message']='calendar_name not provided'

            return Response(response)
    except Exception as e:
        response['message']='exception in api{}'.format(e)
        return Response(response)
