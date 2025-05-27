from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("AgendaLembrete online!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # <- adiciona isso
]
