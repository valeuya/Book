from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem

first_time = True


# Create your views here.
def todoView(request):
    global first_time
    all_todo_items = TodoItem.objects.all()
    if (first_time):
        new_item = TodoItem(content="build a cool app on replit.com")
        new_item.save()
        first_time = False
    return render(request, 'index.html', {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')


def coverImage(request):
    image_data = open("./todo/app.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def CoolerBook(request):
    return render(request, 'CoolerBook.html')


def CoolerBookAboutUs(request):
    return render(request, 'CoolerBookAboutUs.html')


def CoolerBookArticle(request):
    return render(request, 'CoolerBookArticle.html')


def CoolerBookContacts(request):
    return render(request, 'CoolerBookContacts.html')


def CoolerBookRegister(request):
    return render(request, 'CoolerBookRegister.html')

def CoolerBookSuccess(request):
    return render(request, 'CoolerBookSuccess.html')

