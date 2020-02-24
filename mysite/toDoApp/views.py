from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'toDoApp/index.html', {"todo_items": todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_object = Todo.objects.create(added_date=current_date, text=content)
    length_of_todo = Todo.objects.all().count()
    return HttpResponseRedirect("/toDoApp")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/toDoApp")


