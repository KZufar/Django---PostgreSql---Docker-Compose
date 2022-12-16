from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import ClassAnnotation

# Create your views here.
def index(request):
    classes = ClassAnnotation.objects.all()
    context = {'classes': classes}
    print(classes)
    return render(request, 'index.html',context=context)


# сохранение данных в бд
def create(request):
    print("CReate------------")
    if request.method == "POST":
        cls = ClassAnnotation()
        cls.name = request.POST.get("name")
        cls.color = request.POST.get("color")
        cls.save()
    return HttpResponseRedirect("/")
    # return render(request, 'index.html')
        # print('Table: ', cls.objects.all())
