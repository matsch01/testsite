from django.conf.urls import patterns, include, url
from testsite.views import hello,my_homepage_view,current_datetime,hours_ahead,current_datetime_short,display_meta
from testsite.books import views as bookviews
from testsite.contact import views as contactviews

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time_short/$', current_datetime_short),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^display_meta/$', display_meta),
    (r'^search/$', bookviews.search),
    (r'^contact/$', contactviews.contact),
    (r'^$', my_homepage_view),
   
)


print 'blah blah &^%&^&^!'