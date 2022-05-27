from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def todays_photos(request):
    date = dt.date.today()
    return render(request, 'photos/todays_photos.html',{'date': date})



def past_days_photographs(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(todays_photos)

    news = Article.days_news(date)
    return render(request, 'photos/pastphotos.html',{"date": date,"news":news})

def todays_photos(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'photos/todays_photos.html', {"date": date,"news":news})  

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})  

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"photos/article.html", {"article":article})            