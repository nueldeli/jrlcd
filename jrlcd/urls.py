"""jrlcd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeEnView, AboutView, PartnershipView, WdimView, WayForwardView #HomeMainView #HomeBmView

urlpatterns = [
    #path('', HomeMainView.as_view(), name='home_main'),
    path('', HomeEnView.as_view(), name='home_en'),
    #path('home_bm/', HomeBmView.as_view(), name='home_bm'),
    path('about/', AboutView.as_view(), name='about'),
    path('partnership/', PartnershipView.as_view(), name='partnership'),
    path('why_does_it_matter/', WdimView.as_view(), name='wdim'),
    path('way_forward/', WayForwardView.as_view(), name='way_forward'),
    path('ckeditor', include('ckeditor_uploader.urls')), 
    path('admin/', admin.site.urls),
    path('nursery/', include('nursery.urls')),
    path('species/', include('species.urls')),
    path('activity/', include('activity.urls')),
    path('publication/', include('publication.urls')),
    path('forest/', include('forest.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
