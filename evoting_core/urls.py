from django.urls import path, include
from django.contrib import admin
from django.shortcuts import redirect


urlpatterns = [
     path('', lambda request: redirect('login')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
       path('accounts/', include('accounts.urls')),
       path('vote/', include('voting.urls')),
       path('ai/', include('ai_assistant.urls')),
         


]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)