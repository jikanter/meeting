from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meeting.views.home', name='home'),
    # url(r'^meeting/', include('meeting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'rest.views.top'),
    url(r'^r/$', 'rest.views.rest'),
    
    # user management views
    url(r'^(?:register|signup)/$',  'registration.views.signup'),
    url(r'^register/user/create/$', 'registration.views.createuser'),
    url(r'^register/user/add/$',    'registration.views.adduser'),
    url(r'^login/$',                'registration.views.loginuser'),
    url(r'^register/user/login/$',  'registration.views.loginuser'),
    url(r'^register/user/logout/$', 'registration.views.logoutuser'),
    #url(r'^login/invalid_account/$', 'web.views.invalidaccount'),
    #url(r'^login/disabled_account/$', 'web.views.disabledaccount'),
   
    # the following 4 methods are only internal and should not be referenced directly from 
    # any views. use the HTTP methods to reference them indirectly (as the REST pattern would recommend).
    # post is used only for adding resources
    url(r'^POST/([^/]+)/$', 'rest.views.post'),
    # get is used only for showing resources
    url(r'^GET/([^/]+)/$', 'rest.views.get'),
    # put is used only for replacing one resource with another
    url(r'^PUT/([^/+])/$', 'rest.views.put'),
    # delete is used only for removing a resource from the db
    url(r'^DELETE/([^/]+)/$', 'rest.views.delete'),
    
    url(r'^em', 'rest.views.embed')
)
