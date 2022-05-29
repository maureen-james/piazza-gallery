from django.shortcuts import render,redirect
import datetime as dt
from .models import Image,Category,Location
from django.http  import HttpResponse,Http404


# Create your views here.
def index(request):
    categories=Category.get_all_category()
    locations=Location.objects.all
    photos=Image.get_all_images()

   
    return render(request,'photos/images.html',{'photos':photos,'categories':categories,'locations':locations})
def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_images = Image.search_image(search_term)
        print(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def get_category(request,category_id):
    images=Image.filter_by_category(category_id)

    return render (request,'category.html',{'images':images})
def get_location(request,location_id):
    images=Image.filter_by_location(location_id)

    return render (request,'location.html',{'images':images})