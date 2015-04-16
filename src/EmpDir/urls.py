from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^about', 'profiles.views.about', name='about'),
    url(r'^profile', 'profiles.views.profile', name='profile'),
    url(r'^contact', 'contact.views.contact', name='contact'),
    url(r'^checkout', 'checkout.views.checkout', name='checkout'),
    url(r'^emp', 'emp.views.emp', name='emp'),
    url(r'^insert', 'emp.views.insert', name='insert'),
    url(r'^delete/(?P<person_id>\d+)$', 'emp.views.delete', name='delete'),
    url(r'^edit/(?P<person_id>\d+)$', 'emp.views.edit', name='edit'),
    (r'^accounts/', include('allauth.urls')),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)