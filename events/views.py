from django.shortcuts import render, redirect # type: ignore
from .models import Event
from django.contrib.auth.decorators import login_required # type: ignore
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    return render(request, 'home.html')  # Create a template called home.html

@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Event.objects.create(title=title, description=description, date=date, created_by=request.user)
        return redirect('event_list')
    return render(request, 'create_event.html')
@login_required
def event_list(request):
    events = Event.objects.all().order_by('date')  # Fetch and sort events by date
    return render(request, 'event_list.html', {'events': events})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            return redirect('create_event')  # Redirect to create event page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def login(request):
    return render(request, 'login')  # No need for 'events/event_list.html'


