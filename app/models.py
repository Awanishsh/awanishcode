from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_updated = models.DateTimeField(auto_now_add=True)



class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address =models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pic =models.ImageField(upload_to= "app/img/candidate")
    



class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    website = models.CharField(max_length=250,default="")
    description = models.CharField(max_length=500,default="")
    logo_pic = models.ImageField(upload_to="app/img/company")


class JobDetailss(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250)
    Companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.CharField(max_length=500)
    qulification = models.CharField(max_length=250)
    responsibility = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    comapanywebsite = models.CharField(max_length=250)
    Companyemail = models.CharField(max_length=250)
    companycontact = models.CharField(max_length=20)
    salarypachage = models.CharField(max_length=250)
    exprience = models.IntegerField()
    logo = models.ImageField(upload_to="app/img/jobpost",default="")



class ApplyList(models.Model):
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetailss,on_delete=models.CASCADE)
    education = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    min_salary = models.CharField(max_length=50)
    max_salary = models.CharField(max_length=50)
    resume = models.FileField(upload_to="app/resume")
    