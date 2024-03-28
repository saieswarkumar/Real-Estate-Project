from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GetPropertyDetailsForm, GetLocationForm, LocationMapForm
from .models import PropertyDetails, LocationDetails
from geopy.geocoders import Nominatim
from django.core.urlresolvers import reverse
import requests
import urllib
from django.db.models import Count
from agent.models import Chat
from agent.forms import ChatForm
from general.models import Profile

@login_required(login_url='/login/')
def home(request):
    proplist = PropertyDetails.objects.filter(user=request.user)
    data={}
    data['prop_list'] = proplist
    return render(request, 'seller/index.html', data)

@login_required(login_url='/login/')
def chart(request):
    loc=LocationDetails.objects.all().values('propid','locationname').annotate(total=Count('propid')).order_by('propid')
    return render(request, 'seller/chart.html',{'loc':loc})

@login_required(login_url='/login/')
def line(request):
    lc1=LocationDetails.objects.all().values('propid','locationname').annotate(total=Count('propid')).order_by('propid')
    return render(request, 'seller/linechart.html',{'loc':lc1})

@login_required(login_url='/login/')
def uploadPropertyDetails(request):
    form = GetPropertyDetailsForm(request.POST or None, request.FILES)
    if form.is_valid():
        propdet = form.save(commit=False)
        propdet.user = request.user
        propdet.save()
        return redirect('sellers:home')
    return render(request, 'seller/newproperty.html', {'form':form})

@login_required(login_url='/login/')
def locationspot(request):
    form = GetLocationForm(request.POST)
    if form.is_valid():
        address = form.cleaned_data.get('locaddress')
        """locationt = geolocator.geocode(addr)
        lati = locationt.latitude
        loni = locationt.longitude
        gmaps = GoogleMaps(AIzaSyCthblLTE___47JWZjTjKjEfCxq0ofxBCU)
        lat, lng = gmaps.address_to_latlng(address)"""
        api_key="AIzaSyCthblLTE___47JWZjTjKjEfCxq0ofxBCU"
        api_response=requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        if api_response_dict['status'] == 'OK':
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        return redirect('sellers:locationfound',lati=latitude,loni=longitude, address=address.replace(" ",""))
    return render(request, 'seller/mylocation.html',{'form':form})
@login_required(login_url='/login/')
def locationspotfound(request, lati,loni,address):
    form = LocationMapForm(request.POST)
    item = PropertyDetails.objects.filter(user=request.user)
    data={}
    data['lati']=lati
    data['loni']=loni
    data['address']=address
    data['forms']=form
    data['items']=item
    if form.is_valid():
        locpdet = form.save(commit=False)
        locpdet.user = request.user
        locpdet.propid = get_object_or_404(PropertyDetails, pk=request.POST.get('item_id'))
        locpdet.locationname=address
        locpdet.lati=lati
        locpdet.longi=loni
        locpdet.save()
        return redirect('sellers:home')
    return render(request, 'seller/mylocation.html',data)

@login_required(login_url='/login/')
def nearestlocation(request):
    return render(request, 'seller/nearestlocation.html', {'form':form})

@login_required(login_url='/login/')
def aboutprop(request,pk):
    propdet=get_object_or_404(PropertyDetails,pk=pk)
    form =GetPropertyDetailsForm(request.POST or None, instance=propdet)
    if 'updatedet' in request.POST:
        if form.is_valid():
            form.save()
            return redirect('sellers:home')
    elif 'deletedet' in request.POST:
        propdet.delete()
        return redirect('sellers:home')
    return render(request, 'seller/viewproprtydetails.html',{'form':form,'propdet':propdet})

def aboutproploc(request,pk):
    locet = LocationDetails.objects.filter(user=request.user,propid=pk)
    lt=0.0
    lg=0.0
    cnt = 0
    for lo in locet:
        lt = lt+lo.lati
        lg = lg+lo.longi
        cnt = cnt+1
    if cnt != 0:
        latt=lt/cnt
        lonn=lg/cnt
    else:
        latt=0.0
        long=0.0
    data={}
    data['prop_list'] = locet
    data['latt'] = latt
    #data['lonn'] = lonn
    return render(request, 'seller/viewproprtyloc.html',data)

@login_required(login_url='/login/')
def chat(request):
    prof=Profile.objects.filter(user_type='AG')
    chatcheck=False
    data={}
    data['prof'] = prof
    data['chatcheck'] = chatcheck
    return render(request, 'seller/chats.html',data)

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
        return redirect('sellers:chatbegin',uid)
    data={}
    data['form'] = form
    data['prof'] = prof
    data['msgs'] = msgs
    data['uid'] = uid
    data['chatcheck'] = chatcheck
    return render(request,'seller/chats.html',data)