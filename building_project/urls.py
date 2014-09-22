from django.conf.urls import patterns, include, url
from django.contrib import admin
from building_project import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'building_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'building_manager.views.home', name='home'),

    # register log in and out
    url(r'^register/$', 'building_manager.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^profile/$', 'building_manager.views.profile', name='profile'),

    #password reset
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    ### Building
    url(r'^building/$', 'building_manager.views.building', name='building'),
    url(r'^building/add/$', 'building_manager.views.add_building', name='add_building'),
    url(r'^building/(?P<building_id>\w+)/$', 'building_manager.views.view_building', name='view_building'),
    url(r'^building/(?P<building_id>\w+)/edit/$', 'building_manager.views.edit_building', name='edit_building'),
    url(r'^building/(?P<building_id>\w+)/delete/$', 'building_manager.views.delete_building', name='delete_building'),

    ### Apartment
    url(r'^apartment/$', 'building_manager.views.apartment', name='apartment'),
    url(r'^apartment/add/$', 'building_manager.views.add_apartment', name='add_apartment'),
    url(r'^apartment/(?P<apartment_id>\w+)/$', 'building_manager.views.view_apartment', name='view_apartment'),
    url(r'^apartment/(?P<apartment_id>\w+)/edit/$', 'building_manager.views.edit_apartment', name='edit_apartment'),
    url(r'^apartment/(?P<apartment_id>\w+)/delete/$', 'building_manager.views.delete_apartment', name='delete_apartment'),

    ### Renter
    url(r'^renter/$', 'building_manager.views.renter', name='renter'),
    url(r'^renter/add/$', 'building_manager.views.add_renter', name='add_renter'),
    url(r'^renter/(?P<renter_id>\w+)/$', 'building_manager.views.view_renter', name='view_renter'),
    url(r'^renter/(?P<renter_id>\w+)/edit/$', 'building_manager.views.edit_renter', name='edit_renter'),
    url(r'^renter/(?P<renter_id>\w+)/delete/$', 'building_manager.views.delete_renter', name='delete_renter'),


)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

