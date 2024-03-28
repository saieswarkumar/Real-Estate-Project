from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from seller.models import PropertyDetails
from .forms import ChatForm
from seller.forms import GetPropertyDetailsForm
from .models import Chat
from general.models import Profile
from buyer.models import PropertyRequests

@login_required(login_url='/login/')
def home(request):
    proplist = PropertyDetails.objects.all()
    data={}
    data['prop_list'] = proplist
    return render(request,'agent/index.html', data)

@login_required(login_url='/login/')
def buyerrequests(request):
    reqprp=PropertyRequests.objects.all()
    data={}
    data['req_prop']=reqprp
    return render(request,'agent/buyerrequests.html',data)
    
@login_required(login_url='/login/')
def buyerrequests(request):
    reqprp=PropertyRequests.objects.all()
    data={}
    data['req_prop']=reqprp
    return render(request,'agent/buyerrequests.html',data)

@login_required(login_url='/login/')
def updatereq(request,pid):
    propup=PropertyRequests.objects.get(id=pid)
    propup.status="sold"
    propup.save()
    return redirect('agents:buyerrequests')

@login_required(login_url='/login/')
def chat(request):
    prof=Profile.objects.all().exclude(user_type='AG')
    chatcheck=False
    return render(request,'agent/chat.html',{'prof':prof,'chatcheck':chatcheck})

@login_required(login_url='/login/')
def chatbegin(request,uid):
    prof=Profile.objects.all().exclude(user_type='AG')
    form = ChatForm(request.POST)
    chatcheck=True
    msgs=Chat.objects.filter(receiver__in=[uid,request.user.id])
    if form.is_valid():
        chatdet=form.save(commit=False)
        chatdet.user=request.user
        chatdet.receiver=uid
        chatdet.save()
        return redirect('agents:chatbegin',uid)
    data={}
    data['form'] = form
    data['prof'] = prof
    data['msgs'] = msgs
    data['uid'] = uid
    data['chatcheck'] = chatcheck
    return render(request,'agent/chat.html',data)

@login_required(login_url='/login/')
def aboutprop(request,pk):
    propdet=get_object_or_404(PropertyDetails,pk=pk)
    form =GetPropertyDetailsForm(request.POST or None, instance=propdet)
    if 'updatedet' in request.POST:
        if form.is_valid():
            form.save()
            return redirect('agents:home')
    elif 'deletedet' in request.POST:
        propdet.delete()
        return redirect('agents:home')
    return render(request, 'agent/viewpropdet.html',{'form':form,'propdet':propdet})
    
@login_required(login_url='/login/')
def makerequest(request,pid,uid):
    req=get_object_or_404(PropertyDetails,pk=pid)
    req.agents=uid
    req.save(update_fields=["agents"])
    return redirect('agents:home')