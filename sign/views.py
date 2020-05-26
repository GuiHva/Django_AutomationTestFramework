from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # Login
            #response.set_cookie('user', username, 3600) # Add browser cookie
            request.session['user'] = username #save session to browser
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error':'username or password error!'})

# event manage
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user', '') # Read browser cookie
    event_list = Event.objects.all()
    username = request.session.get('user', '') # Read browser session
    return render(request, "event_manage.html", {"user":username,"events": event_list})

@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})

# guest management
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guests = Guest.objects.get_queryset().order_by('id')

    paginator = Paginator(guests, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})

# sign page
@login_required
def sign_index(request, event_id):
    print(event_id)
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)
    guest_data = str(len(guest_list))
    sign_data = 0         
    for guest in guest_list:
        if guest.sign == True:
            sign_data += 1
    return render(request, 'sign_index.html', {'event': event,
                                               'guest': guest_data,
                                               'sign': sign_data})

# sign action
@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)
    guest_data = str(len(guest_list))
    sign_data = 0
    for guest in guest_list:
        if guest.sign == True:
            sign_data += 1

    phone = request.POST.get('phone', '')

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.', 'guest': guest_data, 'sign': sign_data})

    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.', 'guest': guest_data, 'sign': sign_data})

    result = Guest.objects.get(event_id=event_id, phone=phone)

    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "user has sign in.", 'guest': guest_data, 'sign': sign_data})
    else:
        Guest.objects.filter(event_id=event_id, phone=phone).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!',
                                                   'user': result,
                                                   'guest': guest_data,
                                                   'sign': str(int(sign_data)+1)
                                                   })

# Logout
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response