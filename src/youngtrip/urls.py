"""youngtrip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

from youngtrip import settings

from apps.account.views import IndexView

#修改一下后台管理系统名称
admin.site.site_header = '青年游记'
admin.site.site_title = '青年游记管理后台'
admin.site.index_title = '首页'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),

    path('api/account/', include('apps.account.urls')),
    path('api/', include('apps.card.urls')),
    path('api/', include('apps.comment.urls')),
    path('api/', include('apps.like.urls')),
    path('api/', include('apps.fans.urls')),
    path('api/', include('apps.file.urls')),
    path('api/', include('apps.trip.urls')),
    path('api/', include('apps.slide.urls')),

    #ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('api-auth/', include('rest_framework.urls', namespace='rest_framework')))
    urlpatterns.append(path('docs/', include_docs_urls(title='API文档')))
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
