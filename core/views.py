from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RecentWorkSerializer


# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['works'] = RecentWork.objects.all()
        context['clients'] = Client.objects.all()
        return context


class RecentWorkApiView(APIView):
    def get(self, request):
        recentWorks = RecentWork.objects.all()
        serializer = RecentWorkSerializer(recentWorks, many=True)
        return Response({"Recent works": serializer.data})
