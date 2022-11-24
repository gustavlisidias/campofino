from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve 
from personal.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
	re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
	re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Campo Fino'
admin.site.site_title = 'Administração Campo Fino'
admin.site.site_url = 'http://127.0.0.1:8000/'
#'http://recselsystem.com/'
admin.site.index_title = 'Administração Campo Fino'
admin.empty_value_display = '**Empty**'