from django.urls import path,include
from . import views

urlpatterns =[ 
    path("",views.IndexPage,name="index"),
    path("signup/",views.SingupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.otpverify,name="otp"),
    path("loginpage/",views.Loginpage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.profilePage,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("joblist/",views.CandidateJoblistpage,name="joblist"),
    path("apply/<int:pk>",views.Applypage,name="apply"),
    path("applyjob/<int:pk>",views.Applyjob,name="applyjob"),




    ####################Company side##################
    path("companyindex/",views. CompanyIndexpage,name="companyindex"),
    path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>",views.updatecompanyprofile,name="updatecompanyprofile"),
    path("jobpostpage/",views.Jobpostpage,name="jobpostpage"),
    path("jobpost/<int:pk>",views.jobDetailSubmit,name="jobpost"),
    path("jobpostlist",views.Joblistpage,name="joblistpage"),
    path("companylogout",views.companylogout,name="companylogout"),
    path("applyjoblist",views.Jobapplylist,name="applylist"),




################admin side ###############

path("adminloginpage",views.Adminloginpage,name="adminloginpage"),
path("adminindex",views.AdminIndexpage,name="adminindex"),
path("adminlogin",views.Adminlogin,name="adminlogin"),
path("adminuserlist",views.Adminuserlist,name="userlist"),
path("admincompanylist",views.Admincompanylist,name="companylist"),
path("deleteuser/<int:pk>",views.UserDelete,name="deleteuser"),
path("verifycompantpage/<int:pk>",views.VerifyCompanyPage,name="verifypage"),
path("verifycompany/<int:pk>",views.Verifycompany,name="verify"),
path("deletecompany/<int:pk>",views.CompanyDelete,name="deletecompany"),

]

    