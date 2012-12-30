from django.conf.urls import patterns, include, url

# for development
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# For extended registration forms
from customer import regbackend
from customer.profile import UserRegistrationForm
from registration.views import register


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'front_page.html'}),
    url(r'^about$', 'django.views.generic.simple.direct_to_template', {'template': 'about.html'}),
    # url(),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Used for the registration application
    url(r'^accounts/register/$', register, {'backend': 'registration.backends.default.DefaultBackend','form_class': UserRegistrationForm}, name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

# for development
urlpatterns += staticfiles_urlpatterns()