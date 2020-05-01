from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#yaha sare page ka function likhte pura backhand yahi aata aur backend 
#ko transfer krte apne frontend me usein{{ }} in front end

from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

def index(request):
    # return HttpResponse('this is home page') #ye text return krta
   
    '''if we want to return any value f a variable to our html page
    then write the variable beteen {{ }} at html page and the
    backend of variable on this page'''
    
    return render(request, 'index.html')




def portfolio(request):
    #return HttpResponse('this is services page')
    return render(request, 'portfolio.html')


def contact(request):
    #return HttpResponse('this is contact page')
    if request.method== "POST": #agr submit button click hoga
        
        name= request.POST.get('name') #toh yeh sare data le lega
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')
        
        #now pass the value in the model and save it
        contact=Contact(name= name, email= email, subject= subject , 
                        message= message , date=datetime.today())  #data lene ke baad app ke  modelel me table name Contact ke attribute
                                                                #ko fill kr dega
        contact.save()             #fill krne ke baad use database me save kr dega
                                    #ek baar models.py me jake model dekh lo  
        
                                                                     #jab data save ho jayega toh user ko ek sucess msg display kra skte
        #return HttpResponse(allert)    #contact page ke last me submit ke baad waha jaiye ab  

        
        #ek aur tarika hai message diaplay krne ka success hone pe contact page pe
        context = {
        'data':'Your message has been send Successfully!'
         }
        print(context)
        return render(request, 'index.html', context)




# function ka naam directly check hoga us butten ya field se,jaise hi match krega function call ho jayega      

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return render(request, 'index.html')
        
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return render(request, 'index.html')

        # passwords should match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, 'index.html')

        # Create the user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your iCoder account has been successfully created")
        return render(request, 'index.html')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return render(request, 'about.htm') 
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return render(request, 'index.html')
            
    return HttpResponse('404 - Not Found')


def handleLogout(request): 
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return render(request, 'index.html') 





