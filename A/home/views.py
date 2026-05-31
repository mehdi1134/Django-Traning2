from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='user_login')
def home(request):
    todos=Todo.objects.all()
    return render(request, 'home.html', {'todos':todos})
#@login_required
def create(request):
    if request.method == 'POST':
     form = TodoCreateForm(request.POST)
     if form.is_valid():
        cd = form.cleaned_data
        Todo.objects.create(title=cd['title'],body=cd['body'],created=cd['created'])
        messages.success(request,"رکورد شما با موفقیت ثبت گردید")
        return redirect('home')
    else:
     form = TodoCreateForm()
    return render(request, 'create.html', {"form":form})
     
def details(request, todo_id):
    # Get the specific todo item or return 404
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'details.html', {'todo': todo})


def delete_todo(request, todo_id):
    # Get the todo or return 404
    todo = get_object_or_404(Todo, id=todo_id)
    
    # Optional: Add confirmation or permission checks here
    if request.method == 'POST':
        todo.delete()
        messages.success(request, f'"{todo.title}" has been deleted successfully!')
        return redirect('home')
    
    # If GET request (optional: show confirmation page)
    return redirect('home')
    
         


