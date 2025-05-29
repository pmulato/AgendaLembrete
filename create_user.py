import os
import django
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agenda.settings")
django.setup()

username = "Gestor"
password = "PauloMulato"
email = "gestor@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print("Usuário Gestor criado com sucesso.")
else:
    print("Usuário Gestor já existe.")
