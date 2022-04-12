from ast import Return
from email import message
from django.shortcuts import redirect, render
from .models import *
from random import randint
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def SingupPage(request):
    return render(request,"app/signup.html")  


def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']      
        lname = request.POST['lastname']      
        email = request.POST['email'] 
        password = request.POST['password']      
        cpassword = request.POST['cpassword']      


        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp =  randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp, email=email,password=password)
                newcan = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)  
                return render(request,"app/otpverify.html",{'email':email}) 
 


    else:
        if request.POST['role']=="Company":
           role = request.POST['role']
           fname = request.POST['firstname']      
           lname = request.POST['lastname']      
           email = request.POST['email'] 
           password = request.POST['password']      
           cpassword = request.POST['cpassword']      


        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp =  randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp, email=email,password=password)
                newcomp = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)  
                return render(request,"app/otpverify.html",{'email':email}) 
    
     
         
          

def OTPPage(request):
    return render(request,"app/otpverify.html")                



def otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])


    user = UserMaster.objects.get(email=email)

    
    if user:
        if user.otp == otp:
            message = "Otp verify succefully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "Otp is increact"
            return render(request,"app/otpverify.html",{'msg':message})   

    else:
            return render(request,"app/signup.html")     


def Loginpage(request):
    return render(request,"app/login.html")


def LoginUser(request):
    if request.POST['role'] =="Candidate":
        email = request.POST['email'] 
        password = request.POST['password']  


        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                return redirect('index')

            else:
                message = "password doesnot match"
                return render(request,"app/login.html",{'msg':message})
                
        else:
                message ="User doesnot Exist"
                return render(request,"app/login.html",{'msg':message})
    else:
            if request.POST['role'] =="Company":
                email = request.POST['email'] 
                password = request.POST['password']  
 

            user = UserMaster.objects.get(email=email)
            if user:
               if user.password==password and user.role=="Company":
                  can = Company.objects.get(user_id=user)
                  request.session['id'] = user.id
                  request.session['firstname'] = can.firstname
                  request.session['lastname'] = can.lastname
                  request.session['email'] = user.email
                  request.session['password'] = user.password
                  return redirect('companyindex')

            else:
                message = "password doesnot match"
                return render(request,"app/login.html",{'msg':message})
                
def profilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can =  Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user,'can':can})
         
    

def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.contact = request.POST['Contact']
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.address = request.POST['address']
        can.dob = request.POST['dob']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['image']
        can.save()
        url = f'/profile/{pk}'
        return redirect(url)
        
def Applypage(request,pk):

    user = UserMaster.objects.get(pk=pk)
    if user :
        cand = Candidate.objects.get(user_id=user)
        job = JobDetailss.objects.get(id=pk)

    return render(request,"app/apply.html",{'user':user,'cand':cand,'job':job})  

def  Applyjob(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetailss.objects.get(id=pk)
        edu = request.POST['education']
        web = request.POST['website']
        gender = request.POST['gender']
        resume = request.FILES['resume']
        min_salary = request.POST['minsalary']
        max_salary = request.POST['maxsalary']
        
        
        newapply = ApplyList.objects.create(Candidate=cand,job=job,education=edu,gender=gender,website=web,
        min_salary=min_salary,max_salary=max_salary,resume=resume )
        message = "Apply done successfully "
        return render(request,"app/apply.html",{'msg':message})

        
    ############company login #####################   



########################company side##################################

def CompanyIndexpage(request):
    return render(request,"app/company/index.html")



def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    return render(request,"app/company/profile.html",{'user':user,'comp':comp})      

def updatecompanyprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        comp.firstname = request.POST['firstname']   
        comp.lastname = request.POST['lastname']   
        comp.company_name = request.POST['companyname']
        comp.contact = request.POST['contact']  
        comp.state = request.POST['state']   
        comp.city = request.POST['city']   
        comp.website = request.POST['website']   
        comp.address = request.POST['address']   
        comp.description = request.POST['description']   
        comp.logo_pic =request.FILES['image']  
        comp.save()
        url = f'/companyprofile/{pk}'
        return redirect(url)


def Jobpostpage(request):
    return render(request,"app/company/jobpost.html")


def jobDetailSubmit(request,pk):
    user = UserMaster.objects.get(pk=pk)   
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        Companyname =  request.POST['Companyname']
        companyaddress =  request.POST['companyaddress']
        jobdescription =  request.POST['jobdescription']
        qulification =  request.POST['qulification']
        responsibility =  request.POST['responsibility']
        location =  request.POST['location']
        comapanywebsite =  request.POST['comapanywebsite']
        Companyemail =  request.POST['Companyemail']
        companycontact =  request.POST['companycontact']
        salarypachage =  request.POST['salarypachage']
        exprience =  request.POST['exprience']
        logo = request.FILES['image']


        newjob = JobDetailss.objects.create(company_id=comp,jobname=jobname,Companyname=Companyname,companyaddress=companyaddress,jobdescription=jobdescription,
        qulification=qulification,responsibility=responsibility,location=location,comapanywebsite=comapanywebsite,Companyemail=Companyemail,companycontact=companycontact,
        salarypachage=salarypachage,logo=logo,exprience=exprience)

        message = "Job post Successfully"
        return render(request,"app/company/jobpost.html",{'msg':message})




def Joblistpage(request):
    all_job = JobDetailss.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job':all_job})        





def CandidateJoblistpage(request):
    all_job = JobDetailss.objects.all()
    return render(request,"app/job-list.html",{'all_job':all_job}) 




def Jobapplylist(request):
    all_jobapply = ApplyList.objects.all()
    return render(request,"app/company/applyjoblist.html",{'all_job':all_jobapply})        



def companylogout(request):
    del request.session['email']
    del request.session['password']    
    return redirect('index')



########################Admin side ###########################


def Adminloginpage(request):
    return render(request,"app/admin/login.html")


def AdminIndexpage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"app/admin/index.html")

    else:
        return redirect('adminloginpage')


def Adminlogin(request):
    username = request.POST['username']
    password = request.POST['password']   

    if username == "admin" and password == "admin" :
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')

    else:
        message = "username and password not match"  
        return render(request,"app/admin/login.html",{'msg':message})  



def Adminuserlist(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request,"app/admin/userlist.html",{'alluser':all_user})    



def Admincompanylist(request):
    all_company = UserMaster.objects.filter(role="Company")
    return render(request,"app/admin/companylist.html",{'allcompany':all_company})      



def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')     


def VerifyCompanyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"app/admin/verify.html",{'company':company})   




def Verifycompany(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('companylist')



def CompanyDelete(request,pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')  