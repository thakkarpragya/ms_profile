from rest_framework import serializers
from .models import Profile,MasterEdu,WorkExperience,Notes

class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Profile
        fields = (            
            'regId',
	    'stream',
	    'name',
	    'mobile',
	    'email',
	    'roleName',
	    'yearOfJoining',
	    'yearOfPassing',
	    'skills',
	    'interests',
	    'linkedInProfile',
	    'yearsOfExperince',
            'expertise',          
        )  
        
class MasterEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterEdu
        fields = (            
            'regId',
	    'instituteName', 
	    'mastersSubject',
            'yearOfCompletion', 
        )                  
  

class WorkExperienceSerializer(serializers.ModelSerializer):   
    class Meta:
        model = WorkExperience
        fields = (     
            'regId',
	    'company',
	    'startYear',
	    'endYear',
	    'designation',
            'role',          
        )   

        
class TyNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = (            
            'regId',
	    'fromName',
	    'date',
            'note'
        ) 
        
   
class CompleteProfileSerializer(serializers.ModelSerializer):
    
    higheredu = MasterEduSerializer(many=True, required=False)
    workex = WorkExperienceSerializer(many=True, required=False)     
    tyn = TyNotesSerializer(many=True, read_only=True)
    
    class Meta:
        model = Profile
        fields = (            
            'regId',
	    'stream',
	    'name',
	    'mobile',
	    'email',
	    'roleName',
	    'yearOfJoining',
	    'yearOfPassing',
	    'skills',
	    'interests',
	    'linkedInProfile',
	    'yearsOfExperince',
            'expertise',
            'higheredu',
            'workex',
            'tyn',
        )        
 
    def create(self, validated_data):
        higheredu_data = validated_data.pop('higheredu')
    
        workex_data = validated_data.pop('workex')   
            
        # workex_data = validated_data.pop('workex')   
        profile = Profile.objects.create(**validated_data)
        for higheredu_rec in higheredu_data:
            MasterEdu.objects.create(regId=profile,**higheredu_rec)                  
        for workex_rec in workex_data:
            WorkExperience.objects.create(regId=profile,**workex_rec)    
        return profile     
    
    def update(self, instance, validated_data):
        if(validated_data.get('higheredu')):
            higheredu_data = validated_data.pop('higheredu')
        else:
            higheredu_data = []
        
        if(validated_data.get('workex')):
            workex_data = validated_data.pop('workex')   
        else:
            workex_data = []      
        
        # Update profile details
        instance.regId = validated_data.get('regId', instance.regId)
        instance.stream = validated_data.get('stream', instance.stream)
        instance.name = validated_data.get('name', instance.name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)
        instance.roleName = validated_data.get('roleName', instance.roleName)
        instance.yearOfJoining = validated_data.get('yearOfJoining', instance.yearOfJoining)
        instance.yearOfPassing = validated_data.get('yearOfPassing', instance.yearOfPassing)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.interests = validated_data.get('interests', instance.interests)
        instance.linkedInProfile = validated_data.get('linkedInProfile', instance.linkedInProfile)
        instance.yearsOfExperince = validated_data.get('yearsOfExperince', instance.yearsOfExperince)
        instance.expertise = validated_data.get('expertise', instance.expertise)       
        instance.save()        
               
        # Update Higher education details      
        higheredu_with_same_profile_instance = MasterEdu.objects.filter(regId=instance.pk).values_list('id', flat=True)
	
        higheredu_id_pool = []
	
        for higheredu_rec in higheredu_data:
            if "id" in higheredu_rec.keys():            
                # Update existing record                  
                if MasterEdu.objects.filter(id=higheredu_rec['id']).exists():
                    higheredu_instance = MasterEdu.objects.get(id=higheredu_rec['id'])
                    higheredu_instance.instituteName = higheredu_rec.get('instituteName',higheredu_instance.instituteName)
                    higheredu_instance.mastersSubject = higheredu_rec.get('mastersSubject',higheredu.mastersSubject)
                    higheredu_instance.yearOfCompletion = higheredu_rec.get('yearOfCompletion',higheredu.yearOfCompletion)	            	            
                    higheredu_instance.save()
                    higheredu_id_pool.append(higheredu_instance.id)
                else:
                    continue
            else:
                # Add new record  
                higheredu_instance = MasterEdu.objects.create(regId=instance, **higheredu_rec)
                higheredu_id_pool.append(higheredu_instance.id)
	
        for higheredu_id in higheredu_with_same_profile_instance:
            #Delete record 
            if higheredu_id not in higheredu_id_pool:
                MasterEdu.objects.filter(pk=higheredu_id).delete()    
                
        # Update Work Experience details      
        workex_with_same_profile_instance = WorkExperience.objects.filter(regId=instance.pk).values_list('id', flat=True)
	
        workex_id_pool = []
	
        for workex_rec in workex_data:
            if "id" in workex_rec.keys():            
                # Update existing record                  
                if WorkExperience.objects.filter(id=workex_rec['id']).exists():
                    workex_instance = WorkExperience.objects.get(id=workex_rec['id'])
                    workex_instance.company = workex_rec.get('company',workex_instance.company)
                    workex_instance.startYear = workex_rec.get('startYear',workex_instance.startYear)
                    workex_instance.endYear = workex_rec.get('endYear',workex_instance.endYear)          	            
                    workex_instance.designation = workex_rec.get('designation',workex_instance.designation)
                    workex_instance.role = workex_rec.get('role',workex_instance.role)
                    workex_instance.save()
                    workex_id_pool.append(workex_instance.id)
                else:
                    continue
            else:
                # Add new record  
                workex_instance = WorkExperience.objects.create(regId=instance, **workex_rec)
                workex_id_pool.append(workex_instance.id)
	
        for workex_id in workex_with_same_profile_instance:
            #Delete record 
            if workex_id not in workex_id_pool:
                WorkExperience.objects.filter(pk=workex_id).delete()         
                
        return instance
 
 
"""   
class CompleteProfileSerializer(serializers.ModelSerializer):
    
    higheredu = serializers.SerializerMethodField()
    workex = serializers.SerializerMethodField()    
    tyn = serializers.SerializerMethodField()    
    
    class Meta:
        model = Profile
        fields = (            
            'regId',
	    'stream',
	    'name',
	    'mobile',
	    'email',
	    'roleName',
	    'yearOfJoining',
	    'yearOfPassing',
	    'skills',
	    'interests',
	    'linkedInProfile',
	    'yearsOfExperince',
            'expertise',
            'higheredu',
            'workex',
            'tyn',
        )  
    def get_higheredu(self, profile):
        queryset = MasterEdu.objects.filter(regId=profile.regId)
        #return MasterEduSerializer(MasterEdu.objects.all(),many=True).data
        return MasterEduSerializer(queryset,many=True).data
    
    def get_workex(self, profile):
        queryset = WorkExperience.objects.filter(regId=profile.regId)
        return WorkExperienceSerializer(queryset,many=True).data    
    
    def get_tyn(self, profile):
        queryset = Notes.objects.filter(regId=profile.regId)
        return TyNotesSerializer(queryset,many=True).data            
"""   

    

