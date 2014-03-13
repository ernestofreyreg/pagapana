from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pagapana.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pay.views.index'),
    url(r'^registro$', 'pay.views.registro'),
    url(r'^panel$', 'pay.views.panel'),
    url(r'^login$', 'pay.views.entrar'),
    url(r'^logout$', 'pay.views.salir'),

    url(r'^olvido$', 'pay.views.olvido'),
    url(r'^perfil$', 'pay.views.perfil'),

    url(r'^seguridad$', 'pay.infopages.seguridad'),
    url(r'^terminosdelservicio', 'pay.infopages.terminosdelservicio'),
    url(r'^acercade$', 'pay.infopages.acercade'),
    url(r'^contacto$', 'pay.infopages.contacto'),
    url(r'^planes', 'pay.infopages.planes'),
    url(r'^api$', 'pay.infopages.api'),
    url(r'^api/renew$', 'pay.infopages.api_renew'),
    url(r'^api/create$', 'pay.infopages.api_create'),
    url(r'^api/query$', 'pay.infopages.api_query'),
    url(r'^api/info$', 'pay.infopages.api_info'),

    # URL DE PAGO
    url(r'^(.{10})$', 'pay.pago.view'),

)

urlpatterns += staticfiles_urlpatterns()

