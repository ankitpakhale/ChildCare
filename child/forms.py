from django import forms

from .models import lostchild,childinfo,parent,donor
from .models import Post ,Comment,Question,cases

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
	
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
	
class LostForm(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Name'}))
	cityfound=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter City'}))
	age=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Age'}))
	profile_image=forms.ImageField()
	Detail=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Child Details'}))
	guardian=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Guardian Details'}))
    
	class Meta:
		model = lostchild
		fields = ("name", "cityfound","Detail","age", "profile_image", "guardian")

# class LostForm(forms.ModelForm):
# 	class Meta:
# 		model = lostchild
# 		fields = ("__all__")

class ChildForm(forms.ModelForm):
	class Meta:
		model= childinfo
		fields =('name','currentcity','age','cci','guardian','aadhar','dob')

class ParentForm(forms.ModelForm):
	class Meta:
		model=parent
		fields=('__all__')
  
class DonorForm(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your name'}))
	age=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your age'}))
	Gender=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your Gender'}))
	Address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your Address'}))
	Occupation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your Occupation'}))
	Emailid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your Email Id'}))
	Bank_account_no=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your Bank Account No'}))
	IFSC_code=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your IFSC Code'}))
	Aadharcardno=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter your Aadhar Card No'}))
	amount=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Donation Amount'}))

	class Meta:
		model=donor
		fields=(["name", "age", "Gender", "Address", "Occupation", "Emailid", "amount", "Bank_account_no", "IFSC_code", "Aadharcardno"])

class CaseForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter description'}))
	state = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter state'}))
	city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter city'}))
	title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter title'}))
	Address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Address'}))
	class Meta:
		model=cases
		fields=(['description', 'state', 'city', 'title', 'Address'])
  
  