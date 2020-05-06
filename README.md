1.  git clone the https://github.com/ManpraXSoftware/mx-google-calendar.git.
2.  Activate virtual environment and navigate to the folder where the clone has been done.
3.  pip install .
4.  Add "calendar_apis" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [

        'calendar_apis',

    ]

5.  Include the calendar_apis URLconf in your project urls.py like this:

    path('calendar_apis/', include('calendar_apis.urls')),

6.  Add google service account credentials in the Django settings like :
    GOOGLE_CALENDAR_API={
    'client_email':"",
    'private_key' : "-----BEGIN PRIVATE KEY-",
    'private_key_id' : "",
    'client_id' : "",
    }
