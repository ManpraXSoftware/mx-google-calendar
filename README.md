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
    'client_email':"google-calendar-app@striped-antler-275611.iam.gserviceaccount.com",
    'private_key' : "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMu1Z+iRGafcEu\nd+tTqMR8QeWLMVVorSNOvK9rhIlRrPkvVcHtH8L0Kt3+ls1zKzlQ8W7xzxqF6WrM\nPgetVzK77p+GicZOrUiWRycmt0LZHKqsjispLeQ/6dzPw8ikfU/X7KO5zRwWBWVh\nmzoR9HHej7Dz+YlZL/RtQhC7a75+gMdVSm/AcKpVZuLZHb9u//xWl16rFG5WhLV7\nL67/rRW6JcC2piX4UaF+dVyC1Yw1+8BXYfJemZoM2mTIeV8cakfNshQaQTp0aoQh\nyiCSSR5zEy40T9WM5PArZmZI0f7LBSq0Ub47+8kGZ5x4vyzlxCoAVjAT2CsxYVZt\nyI+L+P2lAgMBAAECggEABVe9IsLAuqi7jTV4BGs8CNFT4dkRAaS7Wn606HWVBTH6\n0V/95RQ7ErRgcvD4m6mwhxwKJs5PrxMtNYEMv4vy9pG3Vy+qjtPBENWr08XI7opi\nAzsD8gX4X8p2KSVmaTuTyhrv7/Lt1eYM/zZujFPJyHtcLIw4HhmuY3Z1jno+6OVU\nyotAqgd1wC4NcKvJUl3Gb0ZpHee3sMNuNpCcHKVr03z8cWLvSurOwgKsF2R2D6eW\nPhqgC6/rogdqio+VnUitHAeVTfyyMOFibf74nPBwcfhNJmAJiSl/DGXL3hSkckUa\n2PkQ0bykJGRloYf5iS1GsWmpZ63M8eL2AFPOFX9ZawKBgQDtpp9vBT19u6017XbL\n/muZoqk/KCdpx2Z2iZX0KqQaPGPSih73aZdXNyybK6u8W2LLYUB1dDCPmgYWjSP2\nTKtFgT+CVjCbrEec4pz872Gh4/Rwq0FS1z9yquYWHcRnIb2r8/MfTbF7AxCxnm+2\nwE8kcqFspqT3oGw7Pnpzb481UwKBgQDcigpoI1UmoesU/4DRL3DpVJNoYKfd4sd3\nmY+cdy8aqX/Hw7c6BlbJklgMTiPO+RZ88xlvNo76ZNUPjtI8qDtrCncxsVfBwBaS\nP/lg1gN10dG4tSI2j0PUh8LXslq+p9IhidiGBU0sL2plWGo123vYleQxx3CygTzJ\nfqe2+K7qJwKBgDmC/UpsxjjLVluaoAk2BOwlRTgXi5I5wz4khbmVKCmBO9cTvfK6\nBvoATDcxFlp68yms22CRQb8+0wJaHb3ZSAmGAcyU9yZ1Rs9cuAkuFT6MX/d0OlbF\n6IDjgtMPWRxsOe6HFusYbj8KutuBMB/V4lE7vH0CxyF2HTspH5EYClwpAoGAJ15Q\n+0QLaEkRQP9XTIBOhKh/Y+uVK8vW1afI9iJkezr0v4FVjPsitPr10sSEKedXN1ji\nGnM/1Lz5N7zEFOXnLXWBz5Ib209h+BuJddreZULeUD2tbNXoQuE1S/HftxcYMLp9\nt3bszs1sDclZtGGI2yHuyWAT4xmk80czwzrjZpMCgYEAlccYS/PH0sNiuH4AxIHR\n8rOBpcyaowVXXXtwpN85m7EQQsf3Kfueh/lJ/x81DDufO43oleaz1fNumYN5CBCI\niz593PJFpvqTk/Fr0djlSXdQu1aDztxD7IbX/bdkfpbzHL49FSYIKyRMPN5p37Yw\nwOExACydRWlXvAGwUvOqmgU=\n-----END PRIVATE KEY-----\n",
    'private_key_id' : "a90a38ab28216454259c3dd862f8e4eefc0787db",
    'client_id' : "109937249692533555705",
    }
