from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view()),
    path('api/recent', views.RecentWorkApiView.as_view())
]