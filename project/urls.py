#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns("")

# Admin urls
from django.contrib import admin
admin.autodiscover()

# Custom urls
urlpatterns += patterns("",
    url(r'^', TemplateView.as_view(template_name="pages/home.html"), name="home"),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="pages/robots.txt"), name="robots"),
    url(r'^google.html$', TemplateView.as_view(template_name="pages/google.html"), name="google"),
    url(r'^admin/', include(admin.site.urls)),
)

# Staticfiles urls
if settings.DJANGO_SERVE_PUBLIC:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
