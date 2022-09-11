from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Profile,MasterEdu,WorkExperience,Notes
from .serializers import ProfileSerializer,MasterEduSerializer,WorkExperienceSerializer,TyNotesSerializer,CompleteProfileSerializer
from rest_framework.response import Response
from rest_framework import filters

# Create your views here.

class Profiles(ListCreateAPIView):
    queryset = Profile.objects.all().order_by('-regId')
    serializer_class = ProfileSerializer

class ProfileDetails(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class MasterEd(ListCreateAPIView):
    queryset = MasterEdu.objects.all()
    serializer_class = MasterEduSerializer

class MasterEdDetails(RetrieveUpdateDestroyAPIView):
    queryset = MasterEdu.objects.all()
    serializer_class = MasterEduSerializer
 
class Workex(ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class WorkexDetails(RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer   
    
class TyNotes(ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = TyNotesSerializer

class TyNotesDetails(RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = TyNotesSerializer      

class CompleteProfile(ListCreateAPIView):
    queryset = Profile.objects.all().order_by('-regId')
    serializer_class = CompleteProfileSerializer  

class CompleteProfileDetails(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = CompleteProfileSerializer
    
class FilterProfile(ListAPIView):   
    queryset = Profile.objects.all()
    serializer_class = CompleteProfileSerializer  
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','skills','expertise','higheredu__instituteName','higheredu__mastersSubject','workex__company']
    
  
    
    

  
        

