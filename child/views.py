from django.shortcuts import render ,get_object_or_404,redirect
from django.utils import timezone
from .models import childinfo, userdata,typecci,cci,lostchild,parent,donor,Post ,Comment,cases,Question
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import LostForm ,ChildForm,ParentForm,DonorForm,PostForm,CommentForm,CaseForm
from django.db.models.query_utils import Q
import razorpay


def homepage(request):
	postData = Post.objects.all()
	info=lostchild.objects.all()
	return render(request,"child/homepage.html", {"postData": postData, "info": info})

def lostChild(request):
	info=lostchild.objects.all()
 
	childName = request.GET.get('childName')
	if childName:
		info = lostchild.objects.filter(Q(name__icontains = childName) | Q(age__icontains = childName))
	else:
		info = lostchild.objects.all()
	print(info)
	return render(request,"child/lostChild.html", {"info": info})

def institute(request):
	ins=typecci.objects.all()
	return render(request,"child/institution.html",{"ins":ins})

def special(request):
	info=cci.objects.filter(typ__name__contains="Special Homes")
	return render(request,"child/special.html",{'info':info})

def childlistdl(request):
	info=childinfo.objects.filter(State__contains="Delhi")
	return render(request,"child/delhi.html",{'info':info})

def children(request):
		info=cci.objects.filter(typ__name__contains="Children Home",)
		return render(request,"child/children.html",{'info':info})

def childlistjp(request):
	info=childinfo.objects.filter(State__contains="Jaipur")
	return render(request,"child/jaipur.html",{'info':info})

def place(request):
		info=cci.objects.filter(typ__name__contains="Place")
		return render(request,"child/place.html",{'info':info})

def childlistmb(request):
	info=childinfo.objects.filter(State__contains="Mumbai")
	return render(request,"child/mumbai.html",{'info':info})

def observation(request):
		info=cci.objects.filter(typ__name__contains="Observation Home",)
		return render(request,"child/observation.html",{'info':info})

def childlistkl(request):
	info=childinfo.objects.filter(State__contains="Kolkata")
	return render(request,"child/kolkata.html",{'info':info})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'child/signup.html', {'form': form})


def lost(request):
	info=lostchild.objects.all()
	return render(request,"child/lost.html",{'info':info})


def addlost(request):
	if request.method == "POST":
		form = LostForm(request.POST)
		if form.is_valid():
			child = form.save(commit=False)
			child.save()
			return redirect('lost')
	else:
		form = LostForm()
	return render(request, 'child/addlost.html', {'form': form})


def addchild(request):
	if request.method == "POST":
		# form = ChildForm(request.POST)
		form = LostForm(request.POST)
		if form.is_valid():
			child = form.save(commit=False)
			child.save()
			return redirect('institute')
	else:
		# form = ChildForm()
		form = LostForm()
	return render(request, 'child/addchild.html', {'form': form})


def adoptionlist(request):
	info=childinfo.objects.all()
	return render(request,'child/adoptionlist.html',{'info':info})


def parentform(request):
	if request.method == "POST":
		form = ParentForm(request.POST)
		if form.is_valid():
			child = form.save(commit=False)
			child.save()
			return redirect('adoptionlist')
	else:
		form = ParentForm()
	return render(request, 'child/parentform.html', {'form': form})

def donorform(request):
	if request.method == "POST":
		form = DonorForm(request.POST)
		try:
			userEmail = request.POST['Emailid'].strip()
			if data:=donor.objects.get(Emailid = userEmail):
				return changeDonorData(request, data)
		except Exception:
			if form.is_valid():
				donorData = form.save(commit=False)
				donorData.save()
				return redirect('homepage')
	else:
		form = DonorForm()
	return render(request, 'child/donorform.html', {'form': form})

def changeDonorData(request, data):
	data.amount = request.POST['amount']
	data.Bank_account_no = request.POST['Bank_account_no']
	data.IFSC_code = request.POST['IFSC_code']
	data.Aadharcardno = request.POST['Aadharcardno']
	data.save()
	return redirect('homepage')


def donorPage(request):
	donors = donor.objects.all()
	email = request.GET.get('email')
	if email != None:
		if donor.objects.filter(Emailid = email):
			request.session['email'] = email
			return redirect("paymentdata")
		return render(request, 'child/donorPage.html', {'donors': donors, 'msg': 'Please fill the donor form first'})
	return render(request, 'child/donorPage.html', {'donors': donors})


def paymentData(request):
	if 'email' not in request.session:
		return redirect('donorpage')

	donorData = donor.objects.filter(Emailid=request.session['email'])[0]
	donationAmount = donorData.amount*100
	if request.method == "POST":
		return paymentComplete(donationAmount, request)
	return render(request, 'child/payment.html', {"donorData": donorData, "donationAmount": donationAmount})

def paymentComplete(donationAmount, request):
	# # ---------------------------------------------------------
	client = razorpay.Client(
	auth=("rzp_test_qDwTmKnksUVsaC", "QOr66ZQbsLdNZOmrV4YGX50V"))
	client.order.create({'amount': donationAmount, 'currency': 'INR',
							'payment_capture': '1'})
	# ----------------------------------------------------
	client.order.create({
	'amount': donationAmount,
	'currency': 'INR',
	'payment_capture': '1'
	})
	# ----------------------------------------------------
	# "Saving order data on database"	
	donorData = donor.objects.filter(Emailid=request.session['email'])[0]
	donorData.isPaid = True
	donorData.save()
	del request.session['email']
	# ----------------------------------------------------
	return(redirect('paymentSuccess'))

def paymentSuccess(request):
	mainMsg = "Thank you for donating in child care"
	return render(request, 'child/paymentSuccess.html',{'mainHeading':mainMsg})
    

def post_list(request):
	posts=cases.objects.all()
	
	if request.method == "POST":
		print("post clicked")
		form = CaseForm(request.POST)
		if form.is_valid():
			case = form.save(commit=False)
			case.save()
			return redirect('post_list')
	else:
		form = CaseForm()
	return render(request, 'child/post_list.html', {'form': form, 'posts':posts})
	# return render(request,"child/post_list.html",{})

def post_detail(request, pk):    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'child/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'child/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'child/post_edit.html', {'form': form})




def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')




def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'child/add_comment_to_post.html', {'form': form})




def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)




def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)




def index(request):
    latest_question=Question.objects.order_by("-pub_date")[:5]
    
    context={"latest_question":latest_question}
    return render(request,"child/index.html",context)




def detail(request,pk):
    
    question=get_object_or_404(Question,pk=pk)
    
    return render(request,"blog/detail.html",{"question":question})




