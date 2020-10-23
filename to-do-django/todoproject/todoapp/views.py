from . models import ToDoItem
from django.views.generic import ListView , CreateView , DeleteView , UpdateView
from . forms import CreateToDoForm , EditToDoForm
from django.shortcuts import render , redirect

def IndexView(request):
    return render(request,'index.html')


class HomeView(ListView):
    model = ToDoItem
    template_name = 'home.html'

class CreateToDoView(CreateView):
    model = ToDoItem
    form_class = CreateToDoForm
    template_name = 'add-todo.html'

def DeleteToDoView(request,pk):
    delete_item  = ToDoItem.objects.get(id=pk)
    delete_item.delete()
    return redirect('/home')

class EditToDoView(UpdateView):
    model = ToDoItem
    form_class = EditToDoForm
    template_name = 'edit-todo.html'

def CompleteToDoView(request,pk):
    complete_item = ToDoItem.objects.get(id=pk)
    complete_item.complete = True
    complete_item.save()
    return redirect('/home')
