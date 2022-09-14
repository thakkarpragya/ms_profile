from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Profile(models.Model):
    """
    Profile model added here
    """
    regId = models.CharField(primary_key=True, max_length=8)    
    stream = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    roleName = models.CharField(max_length=20)
    yearOfJoining =  models.DateField(null=True,blank=True)  
    yearOfPassing =  models.DateField(null=True,blank=True)  
    skills = models.CharField(max_length=1000)
    interests = models.CharField(max_length=1000)
    linkedInProfile = models.CharField(max_length=100)
    yearsOfExperince = models.CharField(max_length=5)
    expertise = models.CharField(max_length=1000)
   
    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
        
    def __str__(self):
        return "{}".format(self.regId)
        
class MasterEdu(models.Model):
    """
    Master Education model added here
    """
    regId = models.ForeignKey('Profile',related_name='higheredu',on_delete=models.CASCADE,null=True,blank=True)
    instituteName = models.CharField(max_length=100)
    mastersSubject = models.CharField(max_length=50)
    yearOfCompletion = models.DateField()  
   
    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
        
    def __str__(self):
        return "{}".format(self.regId)      

      
class WorkExperience(models.Model):
    """
    Work Experience model added here
    """
    regId = models.ForeignKey('Profile',related_name='workex',on_delete=models.CASCADE,null=True,blank=True)   
    company = models.CharField(max_length=100)
    startYear = models.DateField()     
    endYear = models.DateField()     
    designation = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
           
    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.    
        """
    
    def __str__(self):
        return "{}".format(self.regId)        
        
class Notes(models.Model):
    """
    Thank You Notes model added here
    """
    regId = models.ForeignKey('Profile', related_name='tyn',on_delete=models.CASCADE)
    fromName = models.CharField(max_length=100)
    date = models.DateField()     
    note = models.CharField(max_length=500)
       
    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
            
    def __str__(self):
        return "{}".format(self.regId)        
         



