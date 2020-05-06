from setuptools import setup

setup(
   name='mx-google-calendar',
   version='1.0',
   description='mx-google-calendar apis',
   author='Kritika Arora',
   author_email='kritika.arora@manprax.com',
   packages=['calendar_apis'],  #same as name
   install_requires=['google-api-python-client', 'google-auth-httplib2','google-auth-oauthlib','oauth2client'], #external packages as dependencies
)
