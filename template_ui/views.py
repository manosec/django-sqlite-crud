from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def crud(request):
    records = User.objects.all
    update = None
    if request.method == 'POST':
        if 'save' in request.POST:
            if request.POST.get('save'):
                pk = request.POST.get('save')
                data = User.objects.get(pk=pk)
                data.name = request.POST.get('name')
                data.score = request.POST.get('score')
                data.save()
            else:
                name = request.POST.get('name')
                score = request.POST.get('score')
                data = User(name=name, score=score)
                data.save()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            data = User.objects.get(pk=pk)
            data.delete()
        else:
            pk = request.POST.get('edit')
            update = User.objects.get(pk = pk)

    return render(request, 'index.html', {
        'records':records,
        'update':update
    })