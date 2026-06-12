from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .models import Apps
# Create your views here.

@login_required
def home(request):

    filter_type = request.GET.get('filter', 'all')

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Apps.objects.create(
                user=request.user,
                title=title
            )
            return redirect('home')

    tasks = Apps.objects.filter(user=request.user)

    if filter_type == 'done':
        tasks = tasks.filter(completed=True)
    elif filter_type == 'progress':
        tasks = tasks.filter(completed=False)

    return render(request, 'home.html', {
        'tasks': tasks,
        'filter_type': filter_type
    })

@login_required
def toggle_task(request, id):
    task = get_object_or_404(
        Apps,
        id=id,
        user=request.user
    )

    task.completed = not task.completed
    task.save()

    return redirect('home')

@login_required
def delete_task(request, id):
    task = get_object_or_404(
        Apps,
        id=id,
        user=request.user
    )

    task.delete()

    return redirect('home')

@login_required
def edit_task(request, id):
    task = get_object_or_404(Apps, id=id, user=request.user)

    if request.method == 'POST':
        new_title = request.POST.get('title')

        if new_title:
            task.title = new_title
            task.save()
            return redirect('home')

    return render(request, 'edit.html', {'task': task})

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })