from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json

# Página de teste padrão
def home(request):
    return HttpResponse("AgendaLembrete online!")

# Endpoint de login via POST
@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
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

# Rotas da aplicação
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/login/', login_api),  # <- endpoint que você quer acessar via curl
]

