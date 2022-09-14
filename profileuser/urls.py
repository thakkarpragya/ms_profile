#from django import views
from django.urls import path
from .views import *

urlpatterns = [   
    path('api/profiles',Profiles.as_view()),   
    path('api/masterEd',MasterEd.as_view()),
    path('api/workex',Workex.as_view()),   
    path('api/completeprofile',CompleteProfile.as_view()),
    path('api/completeprofiledetails/<pk>',CompleteProfileDetails.as_view()),
    path('api/filterprofile',FilterProfile.as_view()),
    path('api/thankyounotes',TyNotes.as_view()),
]