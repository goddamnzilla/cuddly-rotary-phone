from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def index(request):
    
    tickets=Ticket.objects.all().order_by('updated').reverse()
    form=TicketForm()

    if request.method=='POST':
        ticket=Ticket(atm_id=request.POST.get('atm_id'),ticket_details=request.POST.get('ticket_details'),city=request.POST.get('city'),updated_by=request.user.username)
        ticket.save()    
        return redirect('/home')
    
    context = {'tickets':tickets,'form':form}
    return render(request,'incident/list.html', context)

def updateTicket(request, pk):
    
    ticket = Ticket.objects.get(id=pk)
    
    form = TicketForm(instance=ticket)

    if request.method=='POST':
        form = TicketForm(request.POST,instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form':form}
    return render(request,'incident/update_ticket.html',context)

def deleteTicket(request, pk):
    ticket=Ticket.objects.get(id=pk)
    
    if request.method=="POST":
        ticket.delete()
        return redirect('/home')

    context={'ticket':ticket}
    return render(request,'incident/delete.html',context)

def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=email,password=password)
        print(email,password)

        if user is not None:
            login(request,user)
            return redirect('home/')
        else:
            return redirect('/')
        
    return (render(request,'incident/loginpage.html'))

def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password1')
        spassword=request.POST.get('spassword')
        if(password!=spassword or (User.objects.filter(username=email))):
            pass
        else:
            User.objects.create_user(username=email,password=password)
            return redirect('/')
    
    return render(request,'incident/signup.html')

def signout(request):
    logout(request)
    return redirect('/')
