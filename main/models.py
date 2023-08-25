from django.db import models
from django.contrib.auth.models import User

# Create your models here.
form_submitted_choices=(
    ("yes","yes"),
    ("no","no")
)
class Profile(models.Model):
    user_id= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    form_submitted=models.CharField(choices=form_submitted_choices, max_length=50, default="no", null=True, blank=True)




state_choices=(
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh","Arunachal Pradesh"),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),


)

working_choices=(
    ("A Student","A Student"),
    ("A Working employee", "A working employee"),
    ("On Break","On Break"),
)

cat_choices=(
    ("yes","yes"),
    ("no","no"),
)

offer_letter=(
    ("yes","yes"),
    ("no","no"),
    ("not yet", "not yet"),
)

cosigner_choices=(
    ("Father","Father"),
    ("Mother","Mother"),
    ("Guardian","Guardian"),
)
class MyUserForm1(models.Model):
    user_id=models.OneToOneField(User, related_name="User_main1", on_delete=models.CASCADE, null=True, blank=True)
    email= models.CharField( max_length=100)
    phone_no= models.IntegerField()
    state= models.CharField(choices=state_choices, max_length=100)
    city=models.CharField(max_length=100)
    currently_working=models.CharField(choices=working_choices, max_length=50)

class MyUserForm2(models.Model):
    user_id=models.OneToOneField(User, related_name="User_main2", on_delete=models.CASCADE, null=True, blank=True)
    cat_choices=models.CharField(choices=cat_choices, max_length=50)
    class_10th_score=models.IntegerField()
    class_12th_score=models.IntegerField()
    graduation_score=models.IntegerField()
    cat_score=models.CharField(max_length=50)
    offer_letter_qs=models.CharField(choices=offer_letter, max_length=50)
    offer_letter=models.FileField(upload_to="", max_length=100)
    aadhar_card=models.FileField(upload_to="", max_length=100)
    pan_card=models.FileField(upload_to="", max_length=100)
    address_proof=models.FileField(upload_to="", max_length=100)

class MyUserForm3(models.Model):
    user_id=models.OneToOneField(User, related_name="User_main3", on_delete=models.CASCADE, null=True, blank=True)
    co_signer=models.CharField(choices=cosigner_choices, max_length=100)
    cosigner_aadhar=models.FileField(upload_to="", max_length=100)
    cosigner_pan=models.FileField(upload_to="", max_length=100)
    cosigner_address=models.FileField(upload_to="", max_length=100)






# class MyUserForm(models.Model):
#     user_id=models.OneToOneField(User, related_name="User_main", on_delete=models.CASCADE,null=True,blank=True)
#     email= models.CharField( max_length=100, null=True,blank=True)
#     phone_no= models.IntegerField(null=True,blank=True)
#     state= models.CharField(choices=state_choices, max_length=100, null=True,blank=True)
#     city=models.CharField(max_length=100, null=True,blank=True)
#     currently_working=models.CharField(choices=working_choices, max_length=50, null=True,blank=True)
#     cat_choices=models.CharField(choices=cat_choices, max_length=50, null=True,blank=True)
#     class_10th_score=models.IntegerField(null=True,blank=True)
#     class_12th_score=models.IntegerField(null=True,blank=True)
#     graduation_score=models.IntegerField(null=True,blank=True)
#     cat_score=models.CharField(max_length=50,null=True,blank=True )
#     offer_letter_qs=models.CharField(choices=offer_letter, max_length=50,null=True,blank=True )
#     offer_letter=models.FileField(upload_to="", max_length=100, null=True,blank=True)
#     aadhar_card=models.FileField(upload_to="", max_length=100, null=True,blank=True)
#     pan_card=models.FileField(upload_to="", max_length=100, null=True,blank=True)
#     address_proof=models.FileField(upload_to="", max_length=100, null=True,blank=True)
#     co_signer=models.CharField(choices=cosigner_choices, max_length=100,null=True,blank=True)
#     cosigner_aadhar=models.FileField(upload_to="", max_length=100, null=True,blank=True)
#     cosigner_pan=models.FileField(upload_to="", max_length=100, null=True,blank=True)
#     cosigner_address=models.FileField(upload_to="", max_length=100, null=True,blank=True)
