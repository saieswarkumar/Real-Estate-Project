from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from seller.models import PropertyDetails, LocationDetails
from general.models import Profile
from .forms import PropertyRequestsForm
from agent.forms import ChatForm
from .models import PropertyRequests
from agent.models import Chat

@login_required(login_url='/login/')
def home(request):
    proplist = PropertyDetails.objects.all()
    data={}
    data['prop_list'] = proplist
    return render(request, 'buyer/index.html', data)

@login_required(login_url='/login/')
def requestedprops(request):
    reqprp=PropertyRequests.objects.filter(user=request.user).select_related() 
    data={}
    data['req_prop']=reqprp
    return render(request,'buyer/requestedprops.html',data)

@login_required(login_url='/login/')
def chat(request):
    prof=Profile.objects.filter(user_type='AG')
    chatcheck=False
    data={}
    data['prof'] = prof
    data['chatcheck'] = chatcheck
    return render(request,'buyer/chats.html',data)

@login_required(login_url='/login/')
def chatbegin(request,uid):
    prof=Profile.objects.filter(user_type='AG')
    form = ChatForm(request.POST)
    msgs=Chat.objects.filter(receiver__in=[uid,request.user.id])
    chatcheck=True
    if form.is_valid():
        chatdet=form.save(commit=False)
        chatdet.user=request.user
        chatdet.receiver=uid
        chatdet.save()
        return redirect('buyers:chatbegin',uid)
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
    if propdet.agents==0:
        agentdet=Profile.objects.none()
    else:
        agentdet=get_object_or_404(Profile,pk=propdet.agents)
    locdet=LocationDetails.objects.filter(propid_id=pk)
    lt=0.0
    lg=0.0
    cnt = 0
    for lo in locdet:
        lt = lt+lo.lati
        lg = lg+lo.longi
        cnt = cnt+1
    if cnt != 0:
        latt=lt/cnt
        lonn=lg/cnt
    else:
        latt=0.0
        long=0.0
    form=PropertyRequestsForm(request.POST or None)
    if form.is_valid():
        prop=form.save(commit=False)
        prop.user=request.user
        prop.requestedProperty=PropertyDetails.objects.get(id=pk)
        prop.save()
        return redirect('buyers:home')
    
    data={}
    data['prop_list'] = propdet
    data['agent_det'] = agentdet
    data['loc_det'] = locdet
    data['latt'] = latt
    data['lonn'] = lonn
    data['form'] = form
    return render(request, 'buyer/viewproprtydetails.html',data)

@login_required(login_url='/login/')
def chart(request):
    proplist = PropertyDetails.objects.all()
    data={}
    data['prop_list'] = proplist
    return render(request, 'buyer/chart.html', data)