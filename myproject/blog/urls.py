from django.urls import path
from .views import home, api, articles

app_name='blog'
urlpatterns= [
    path('', home, name='home'),
    path('api', api, name='api'),
    path('articles', articles, name='articles')

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
