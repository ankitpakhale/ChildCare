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
	name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Your Name'}))
	cityfound=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Your City'}))
	Detail=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Your Detail'}))
	age=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Your Age'}))
    
	class Meta:
		model = lostchild
		fields = ('name', 'cityfound',"Detail",'age')

class ChildForm(forms.ModelForm):
	class Meta:
		model= childinfo
		fields =('name','currentcity','age','cci','guardian','aadhar','dob')

class ParentForm(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Name'}))
	age=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Age'}))
	Gender=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Gender'}))
	Martialstatus=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Martial Status'}))
	city=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter City'}))
	state=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter State'}))
	Job_description=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Job Description'}))
	adoptionreason=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Adoption Reason'}))
	aadhar=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Aadhar No'}))
	childwanted=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'Enter Child Details'}))
	class Meta:
		model=parent
		fields=(['name','age','Gender','Martialstatus','city','state','Job_description','adoptionreason','aadhar', 'childwanted'])

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
  
  