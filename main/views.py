from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, Http404, HttpResponse, HttpResponseNotFound
from .forms import Signupform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import userform1, userform2, userform3
from .models import  Profile, MyUserForm1, MyUserForm2, MyUserForm3


# Create your views here.
def index(request):
    return render(request, "index.html")

def sign_up(request):
    form=Signupform()
    if request.method=="POST":
        form=Signupform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request, user)
            return redirect("dashboard")



    context={
        "form":form,

    }
    return render(request, "signup.html", context)



def log_in(request):
    message=""

    if request.method=="POST":
        
        try:         
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=User.objects.get(username=username)

            if user is not None:
                user=authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    message="Entered password is wrong"
        
        
        except:
            message="username or password is wrong"
    context={
        "message":message
    }

    return render(request, "login.html",context)

@login_required(login_url="/sign-in/")
def log_out(request):
    logout(request)
    return redirect("sign-in")

@login_required(login_url="/sign-in/")
def dashboard(request):
    return render(request, "dashboard.html")

@login_required(login_url="/sign-in/")
def registration1(request):
    try:
        profile=Profile.objects.get(user_id__username=request.user)
        if profile.form_submitted=="yes":
            return redirect("form-submitted")
    except:
        pass        

    try:
        user_submitted=MyUserForm1.objects.get(user_id__username=request.user)
    except:
        user_submitted=None
    if user_submitted:
        form=userform1(instance=user_submitted)
    else:
        form=userform1()
    if request.method=="POST":
        print(request.POST)
        if user_submitted:
            form=userform1(request.POST, instance=user_submitted,)
            if form.is_valid():
                print("valid")
                myform=form.save(commit=False)
                myform.user_id=request.user
                myform.save()
                return redirect("registration2")
            else:
                print("form is not valid")
                
            
        else:
            form=userform1(request.POST)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.user_id=request.user
                myform.save()
                return redirect("registration2")
            else:
                print("form is not valid")

    #all data submitted flag

    

    context={
        "form":form,
    }
    return render(request,"registration1.html", context)


@login_required(login_url="/sign-in/")
def registration2(request):
    try:
        profile=Profile.objects.get(user_id__username=request.user)
        if profile.form_submitted=="yes":
            return redirect("form-submitted")
    except:
        pass               

    try:
        user_submitted=MyUserForm2.objects.get(user_id__username=request.user)
    except:
        user_submitted=None
    if user_submitted:
        form=userform2(instance=user_submitted)
    else:
        form=userform2()
    if request.method=="POST":
        if user_submitted:
            form=userform2(request.POST, request.FILES, instance=user_submitted,)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.user_id=request.user
                myform.save()
                print(myform)
                return redirect("registration3")
        else:
            form=userform2(request.POST, request.FILES)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.user_id=request.user
                myform.save()
                return redirect("registration3")

    #all data submitted flag

    

    context={
        "form":form,
    }
    return render(request,"registration2.html", context)




@login_required(login_url="/sign-in/")
def registration3(request):
    form_submitted="no"       

    try:
        user_submitted=MyUserForm3.objects.get(user_id__username=request.user)
    except:
        user_submitted=None
    if user_submitted:
        form=userform3(instance=user_submitted)
    else:
        form=userform3()
    if request.method=="POST":
        form_submitted="yes"

        if user_submitted:
            form=userform3(request.POST, request.FILES, instance=user_submitted,)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.user_id=request.user
                myform.save()
                if form_submitted=="yes":
                    profile=Profile.objects.get(user_id__username=request.user)
                    profile.form_submitted="yes"
                    profile.save()

                return redirect("registration1")
        else:
            form=userform3(request.POST, request.FILES)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.user_id=request.user
                myform.save()
                if form_submitted=="yes":
                    profile=Profile.objects.get(user_id__username=request.user)
                    profile.form_submitted="yes"
                    profile.save()
                return redirect("registration1")

    #all data submitted flag

    context={
        "form":form,
    }
    return render(request,"registration3.html", context)



def form_submitted(request):
    try:
        profile=Profile.objects.get(user_id__username=request.user)
        if profile.form_submitted=="no":
            return redirect("registration1")
    except:
        pass        

    return render(request, "dashboardApplied.html")

# @login_required(login_url="/sign-in/")
# def registration(request):
#     print(request.user)            

#     try:
#         user_submitted=MyUserForm.objects.get(user_id__username=request.user)
#     except:
#         user_submitted=None
#     if user_submitted:
#         form=userform(instance=user_submitted)
#     else:
#         form=userform()
#     if request.method=="POST":
#         if user_submitted:
#             form=userform(request.POST, request.FILES, instance=user_submitted,)
#             if form.is_valid():
#                 myform=form.save(commit=False)
#                 myform.user_id=request.user
#                 myform.save()
#                 print("forma")
#                 return redirect("registration1")
                
            
#         else:
#             form=userform(request.POST, request.FILES)
#             if form.is_valid():
#                 myform=form.save(commit=False)
#                 myform.user_id=request.user
#                 myform.save()
#                 print("formb")
#                 return redirect("registration1")

#     #all data submitted flag

#     l1=[]
#     try:
#         obj=MyUserForm.objects.get(user_id__username=request.user)
#         l1.append(obj.user_id)
#         l1.append(obj.currently_working)
#         l1.append(obj.email)
#         l1.append(obj.phone_no)
#         l1.append(obj.state)
#         l1.append(obj.city)
#         l1.append(obj.currently_working)
#         l1.append(obj.cat_choices)
#         l1.append(obj.class_10th_score)
#         l1.append(obj.class_12th_score)
#         l1.append(obj.graduation_score)
#         l1.append(obj.cat_score)
#         l1.append(obj.offer_letter_qs)
#         l1.append(obj.offer_letter)
#         l1.append(obj.aadhar_card)
#         l1.append(obj.pan_card)
#         l1.append(obj.address_proof)
#         l1.append(obj.co_signer)
#         l1.append(obj.cosigner_aadhar)
#         l1.append(obj.cosigner_pan)
#         l1.append(obj.cosigner_address)


#         if None not in l1:
#             pass 
#         else:
#             pass
#     except:
#         pass

#     context={
#         "form":form,
#     }
#     return render(request,"registration.html", context)



    







