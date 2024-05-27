from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Videos,UserProfile
from django.contrib.auth.models import User, auth,AbstractUser
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def index(request):
    videos = list(Videos.objects.all())
    random.shuffle(videos)
    profile_pic = None  # Initialize as None
    
    if request.user.is_authenticated:  # Check if the user is authenticated
        try:
            profile_pic = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            pass

    context ={
        'videos' : videos[:12],
        'profile_pic' : profile_pic
    }
    
    return render(request,'index.html', context)

def video(request , pk):
    profile_pic = None
    video = Videos.objects.get(id=pk)

    if request.user.is_authenticated:  # Check if the user is authenticated
        try:
            profile_pic = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            pass

    context ={
        'video' : video,
        'profile_pic' : profile_pic
    }

    return render(request ,'video.html',context)

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        username = email
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('signin')
  
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            else:
                username = email
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                # Create a user profile without the profile picture initially
                user_profile = UserProfile.objects.create(user=user)

                return redirect('signin')
        else:
            messages.info(request, "Password does not match")
            return redirect('signup')

    else:
        return render(request, 'signup.html')
    
def upload_profile_pic(request):
    if request.method == 'POST' and 'profile_pic' in request.FILES:
        profile_pic = request.FILES['profile_pic']

        # Get the user's profile and update the profile picture
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.profile_picture = profile_pic
        user_profile.save()

    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/') 