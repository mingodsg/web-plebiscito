from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.IndexView.as_view(), name='index'),
]


