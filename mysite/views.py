from django.http import Http404, HttpResponse
import datetime


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, hour):
    try:
        hour = int(hour)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=hour)
    html = "<html><body>In %s hour(s), it will be %s. </body></html>" % (hour, dt)
    return HttpResponse(html)

