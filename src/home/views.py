from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit


this_dir=pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args, **kwargs):

    return about_view(request,*args, **kwargs)



def about_view(request,*args, **kwargs):
    
    qs= PageVisit.objects.all()
    page_qs= PageVisit.objects.filter(path=request.path)
    print(this_dir)
    my_title= "home page"
    my_context={  
        "page_title": my_title,
        "queryset" : page_qs.count(),
        "percent": page_qs.count() * 100.0 / qs.count(),
        "total_visit_count":qs.count(),
    }
    path= request.path
    print("path",path)
    html_=''
    html_template='home.html'
    PageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)