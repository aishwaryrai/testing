from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Event
from .forms import EventForm


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_details.html', {'event': event, 'user': request.user})

@user_passes_test(lambda u: u.is_staff)
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
@login_required
def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@user_passes_test(lambda u: u.is_staff)
@login_required
def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event})


# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'events/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required
def register_for_event(request, event_id):
    event = Event.objects.get(id=event_id)
    user = request.user

    # Add user to the registered_users if not already registered
    if user not in event.registered_users.all():
        event.registered_users.add(user)
        event.save()

        # Send email notification
        subject = 'Event Registration Confirmation'
        message = (
            f'Dear {user.username},\n\n'
            f'You have successfully registered for the event: {event.title}.\n\n'
            f'Event Details:\n'
            f'Date: {event.date}\n'
            f'Time: {event.time}\n'
            f'Location: {event.location}\n\n'
            'Thank you!'
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, 'You have successfully registered for this event. A confirmation email has been sent.')
        messages.set_level(request, messages.SUCCESS)
    else:
        messages.info(request, 'You are already registered for this event.')

    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))

@login_required
def my_registered_events(request):
    events = Event.objects.filter(registered_users=request.user)
    return render(request, 'events/my_registered_events.html', {'events': events})

@login_required
def unregister_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    if user in event.registered_users.all():
        event.registered_users.remove(user)
        messages.success(request, 'You have been unregistered from the event.')
        messages.set_level(request, messages.SUCCESS)

    return redirect('event_detail', event_id=event.id)
