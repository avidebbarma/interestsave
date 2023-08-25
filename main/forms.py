from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUserForm1, MyUserForm2, MyUserForm3


class Signupform(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Override default widget attributes for input fields
        self.fields['username'].widget.attrs.update({
            
            'id': 'username',
            'class': "form-control input",
            'placeholder':""
            
        })
        self.fields['email'].widget.attrs.update({
            
            'id': 'email',
            'class': "form-control input",
            
        })

        self.fields['password1'].widget.attrs.update({
            
            'id': 'password',
            'class': 'form-control input'
            
        })

        self.fields['password2'].widget.attrs.update({
            
            'id': 'password',
            'class':'form-control input'
            
        })


    class Meta:
        model=User
        fields=("username", "email", "password1", "password2")
                # Override default widget attributes for input fields

class userform1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Override default widget attributes for input fields
        self.fields['email'].widget.attrs.update({
            
            'id': 'email',
            'class': "form-control input",
            'placeholder':"enter your mail"
            
        })
        self.fields['phone_no'].widget.attrs.update({
            
            'id': 'email',
            'class': "form-control input",
            
        })

        self.fields['state'].widget.attrs.update({
            
            'id': 'state',
            'class': 'form-control input'
            
        })

        self.fields['city'].widget.attrs.update({
            
            'id': 'city',
            'class':'form-control input'
            
        })
        self.fields['currently_working'].widget.attrs.update({
            
            'id': '',
            'class': "form-control input",
            'placeholder':"",
            
        })


    class Meta:
        model=MyUserForm1
        fields="__all__"

class userform2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Override default widget attributes for input fields

        self.fields['cat_choices'].widget.attrs.update({
            
            'id': 'exam-preparation',
            'class': "form-control",
            
        })

        self.fields['class_10th_score'].widget.attrs.update({
            
            'id': '',
            'class': 'form-control input'
            
        })

        self.fields['class_12th_score'].widget.attrs.update({
            
            'id': '',
            'class':'form-control input'
            
        })
        self.fields['graduation_score'].widget.attrs.update({
            
            'id': '',
            'class': "form-control input",
            'placeholder':""
            
        })
        self.fields['cat_score'].widget.attrs.update({
            
            'id': '',
            'class': "form-control input",
            
        })

        self.fields['offer_letter_qs'].widget.attrs.update({
            
            'id': '',
            'class': 'form-control'
            
        })

        self.fields['offer_letter'].widget.attrs.update({
            
            'id': 'file',
            
        })
        self.fields['aadhar_card'].widget.attrs.update({
            
            'id': 'file',
   
            
        })
        self.fields['pan_card'].widget.attrs.update({
            
            'id': 'file',
            
        })

        self.fields['address_proof'].widget.attrs.update({
            
            'id': 'file',
            
        })



    class Meta:
        model=MyUserForm2
        fields="__all__"


class userform3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Override default widget attributes for input fields

        self.fields['co_signer'].widget.attrs.update({
            
            'id': 'exam-preparation',
            'class':'form-control'
            
        })
        self.fields['cosigner_aadhar'].widget.attrs.update({
            
            'id': 'file',
            
        })

        self.fields['cosigner_pan'].widget.attrs.update({
            
            'id': 'file',
            
        })
        self.fields['cosigner_address'].widget.attrs.update({
            
            'id': 'file',
            
        })



    class Meta:
        model=MyUserForm3
        fields="__all__"



# class userform(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     # Override default widget attributes for input fields
#         self.fields['email'].widget.attrs.update({
            
#             'id': 'email',
#             'class': "form-control input",
#             'placeholder':"enter your mail"
            
#         })
#         self.fields['phone_no'].widget.attrs.update({
            
#             'id': 'email',
#             'class': "form-control input",
            
#         })

#         self.fields['state'].widget.attrs.update({
            
#             'id': 'state',
#             'class': 'form-control input'
            
#         })

#         self.fields['city'].widget.attrs.update({
            
#             'id': 'city',
#             'class':'form-control input'
            
#         })
#         self.fields['currently_working'].widget.attrs.update({
            
#             'id': '',
#             'class': "form-control input",
#             'placeholder':"",
            
#         })
#         self.fields['cat_choices'].widget.attrs.update({
            
#             'id': 'exam-preparation',
#             'class': "form-control",
            
#         })

#         self.fields['class_10th_score'].widget.attrs.update({
            
#             'id': '',
#             'class': 'form-control input'
            
#         })

#         self.fields['class_12th_score'].widget.attrs.update({
            
#             'id': '',
#             'class':'form-control input'
            
#         })
#         self.fields['graduation_score'].widget.attrs.update({
            
#             'id': '',
#             'class': "form-control input",
#             'placeholder':""
            
#         })
#         self.fields['cat_score'].widget.attrs.update({
            
#             'id': '',
#             'class': "form-control input",
            
#         })

#         self.fields['offer_letter_qs'].widget.attrs.update({
            
#             'id': '',
#             'class': 'form-control'
            
#         })

#         self.fields['offer_letter'].widget.attrs.update({
            
#             'id': 'file',
            
#         })
#         self.fields['aadhar_card'].widget.attrs.update({
            
#             'id': 'file',
   
            
#         })
#         self.fields['pan_card'].widget.attrs.update({
            
#             'id': 'file',
            
#         })

#         self.fields['address_proof'].widget.attrs.update({
            
#             'id': 'file',
            
#         })

#         self.fields['co_signer'].widget.attrs.update({
            
#             'id': 'exam-preparation',
#             'class':'form-control'
            
#         })
#         self.fields['cosigner_aadhar'].widget.attrs.update({
            
#             'id': 'file',
            
#         })

#         self.fields['cosigner_pan'].widget.attrs.update({
            
#             'id': 'file',
            
#         })
#         self.fields['cosigner_address'].widget.attrs.update({
            
#             'id': 'file',
            
#         })



#     class Meta:
#         model=MyUserForm
#         fields="__all__"




