from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render(request, 'current_datetime.html', locals())


def hours_ahead(request, hour):
    try:
        hour = int(hour)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=hour)
    html = "<html><body>In %s hour(s), it will be %s. </body></html>" % (hour, dt)
    return HttpResponse(html)

