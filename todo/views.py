from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        Todo.objects.create(
            subject=request.POST['subject'],
            notes=request.POST['notes']
        )
        return redirect('/')
    return render(request, 'add_edit.html')

def edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.subject = request.POST['subject']
        todo.notes = request.POST['notes']
        todo.save()
        return redirect('/')
    return render(request, 'add_edit.html', {'todo': todo})

def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/')
