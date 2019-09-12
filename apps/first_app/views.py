from django.shortcuts import render, redirect
from django.contrib import messages
from .models import tv

def base (request):
    context={
        "all_tvs" : tv.objects.all(),
    }
    return render (request, "first_app/base.html", context)


def display (request):
    return render (request, "first_app/create.html")


def create (request):
    if request.method == 'POST':
        title=request.POST["title"]
        network=request.POST["network"]
        release_date=request.POST["release_date"]
        tv.objects.create(title=title,network=network,release_date=release_date)
        x = tv.objects.last().id
    return redirect ("/show/"+str(x))


def show(request, show_id):
    context = {
        "show" : tv.objects.get(id=show_id),
    } 
    return render(request,"first_app/show.html", context)

def edit (request, show_id):
    context = {
        "show" : tv.objects.get(id=show_id),
    } 
    return render (request, "first_app/edit.html", context)

def update (request, show_id):
    errors = tv.objects.basic_validator(request.POST)
    id=show_id

    if (len(errors))>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/show/'+id+'/edit')
    else:
        x=tv.objects.get(id=show_id)
        
        x.title=request.POST["title"]
        x.network=request.POST["network"]
        x.release_date=request.POST["release_date"]
        x.description=request.POST["description"]
        x.save()
        messages.success(request, 'TV show updated succesfully!!!')

    return redirect ("/show/"+id)


def delete(request, show_id):
    x = tv.objects.get(id=show_id)
    x.delete()

    return redirect('/')
  
