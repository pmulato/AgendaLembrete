from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import json

# Página inicial
def home(request):
    return HttpResponse("AgendaLembrete online!")

# API de login tradicional
@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                return JsonResponse({'success': True, 'message': 'Autenticado com sucesso!'})
            else:
                return JsonResponse({'success': False, 'message': 'Usuário ou senha inválidos.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/login/', login_api),  # login simples
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # JWT Refresh
]

