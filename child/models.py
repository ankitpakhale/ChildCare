from django.db import models
from django.utils import timezone
import datetime
import os

class typecci(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return (self.name)

class cci(models.Model):
	name=models.CharField(max_length=50)
	typ=models.ForeignKey('child.typecci',related_name="list_of_cci",on_delete=models.CASCADE)
	currentcity=models.CharField(max_length=50)
	no_of_children=models.IntegerField(null=True,blank=True)

	def __str__(self):
		return (self.name)


class childinfo(models.Model):
	statechoice=(('Delhi','DELHI'),('Mumbai',"MUMBAI"),('Ahmedabad',"Ahmedabad"),('Kolkata',"KOLKATA"))
	name=models.CharField(max_length=50)
	currentcity=models.CharField(max_length=10,choices=statechoice,default="Not known")
	cci=models.ForeignKey('child.cci',related_name="list_of_children",on_delete=models.CASCADE)
	aadhar=models.BooleanField(default=False)
	dob = models.DateField(max_length=8)
	age = models.IntegerField(null=True,blank=True)
	profile_image = models.ImageField(upload_to='childs', blank=True, null=True)
	guardian=models.CharField(max_length=50)

	def __str__(self):
		return self.name

class userdata(models.Model):
	userid=models.CharField(max_length=10,primary_key=True)
	username=models.CharField(max_length=20)

class lostchild(models.Model):
	name=models.CharField(max_length=50)
	cityfound=models.CharField(max_length=50)
	age = models.IntegerField(null=True,blank=True)
	

	# def __str__(self):
	# 	today = date.today()
	# 	age = today.year - dob.year
	# 	if today.month < dob.month or today.month == dob.month and today.day < dob.day:
	# 		age -= 1
	# 	return self.age


	profile_image = models.ImageField(upload_to='lostchild', blank=True, null=True)
	Detail=models.CharField(max_length=100000)
	guardian=models.CharField(max_length=50)
	def __str__(self):
		return self.name

class parent(models.Model):
	Sexchoice=(('male','MALE'),
		('female','FEMALE'),
		('other','OTHER')
		)
	martialchoice=(('Married','MARRIED'),
		('unmarried','UNMARRIED'),
		('divorced','DIVORCED'),
		)

	name=models.CharField(max_length=25)
	age=models.IntegerField(null=True,blank=True)
	Gender=models.CharField(max_length=10,choices=Sexchoice,default=None)
	Martialstatus=models.CharField(max_length=10,choices=martialchoice,default="unmarried")
	city=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	Job_description=models.CharField(max_length=5000)
	adoptionreason=models.CharField(max_length=5000)
	aadhar=models.BooleanField(default=False)
 
	childwanted=models.ForeignKey(childinfo,related_name='childwanted',on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class donor(models.Model):
	name=models.CharField(max_length=25)
	Sexchoice=(('male','MALE'),
		('female','FEMALE'),
		('other','OTHER')

		)
	age=models.IntegerField(null=True,blank=True)
	Gender=models.CharField(max_length=10,choices=Sexchoice,default=None)
	Address=models.CharField(max_length=500)
	Occupation=models.CharField(max_length=50)
	Emailid=models.CharField(max_length=50)

	amount=models.IntegerField(max_length=25)
	Bank_account_no=models.CharField(max_length=25)
	IFSC_code=models.CharField(max_length=20)
	Aadharcardno=models.CharField(max_length=20)
	isPaid=models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Post(models.Model):
	author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title
	
	def approved_comments(self):
	    return self.comments.filter(approved_comment=True)
	
class Comment(models.Model):
    post = models.ForeignKey('child.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField("date published")
 	
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now=timezone.now()
		return now-datetime.timedelta(days=1)<=self.pub_date<=now

class cases(models.Model):
	description=models.TextField()
	state=models.CharField(max_length=25)
	city=models.CharField(max_length=30)
	title=models.CharField(max_length=30)
	Address=models.TextField()	

	def __str__(self):
		return self.title