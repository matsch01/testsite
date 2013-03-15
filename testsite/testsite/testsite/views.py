from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world Brah!")

def my_homepage_view(request):
    return HttpResponse('Welcome to my Homepage')

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('dateapp/current_date.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def current_datetime_short(request):
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_date.html', locals())

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('dateapp/hours_ahead.html', locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))