# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def news(request):
	news_list = News.objects.all()
	paginator = Paginator(news_list, 2) 

	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		news = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		news = paginator.page(paginator.num_pages)

	return render_to_response("lfweb/news.html",{"news": news},context_instance=RequestContext(request))

