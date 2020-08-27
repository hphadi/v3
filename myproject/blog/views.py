from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


def home(request):
    homeContext = {
        "user" : "hadi",
        "age" : 42,
        "job" : "programmer"

    }
    #return HttpResponse("Hello, world , this is a blog in Django")
    return render(request, "blog/home.html", homeContext)


def articles(request):
    articlesContext ={
        "articles": [
        {
        "img":"i:this is a sample image",
        "title":"t:this is a sample title",
        "description":"d: this is a sample description to show json as a field in page"
        },
        {"img":         "https://res.cloudinary.com/practicaldev/image/fetch/s--0x1CVm7v--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://static.djangoproject.com/img/logos/django-logo-negative.png",
        "title":        "Announcement of Technical Board Election Registration",
        "description":  "As part of the changes to how Django is governed, it is time to have an election of the Technical Board. See DEP-10 for details."
        },
        {"img":         "https://i0.wp.com/blog.knoldus.com/wp-content/uploads/2020/06/python-django.png?w=1620&ssl=1",
        "title":        "DjangoCon Australia 2020: Schedule live and tickets on sale",
        "description":  "Posted by Katie McLaughlin and Markus Holtermann on August 14, 2020"
        },
        {"img":         "https://media.geeksforgeeks.org/wp-content/uploads/20200210175202/django-basics.png",
        "title":        "Django 3.1 Released",
        "description":  "Posted by Mariusz Felisiak on August 4, 2020"
        }
        ]
    }
################


    return render(request,"blog/articles.html",articlesContext)


def api(request):
    data = {
        "1":{
            "Film Name":"film1",
            "id":20,
            "Genre":"genre1"
        },
        "2":{
            "Film Name":"film2",
            "id":21,
            "Genre":"genre2"
        },
        "3":{
            "Film Name":"film3",
            "id":22,
            "Genre":"genre3"},
        }
    return JsonResponse(data)
