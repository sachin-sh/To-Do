from django.shortcuts import render ,redirect
from .models import todo
from django.contrib import messages
from .forms import todoform

def index(request):

    item=todo.objects.order_by("-date")
    if request.method=="POST":
        form =todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form=todoform()

    context={
        "forms":form,
        "list" :item,
        "title":"Todo_List"
    }
    return render(request,"index.html",context)

def remove(request,item_id):
    item=todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
