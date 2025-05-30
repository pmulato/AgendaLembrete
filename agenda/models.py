from django.db import models
from django.contrib.auth.models import User  # <- adicione isso

class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # <- novo campo
    nome_cliente = models.CharField(max_length=100)
    servico = models.CharField(max_length=200)
    data = models.DateField()

    AVISOS = [
        ('7', '7 dias'),
        ('15', '15 dias'),
        ('30', '30 dias'),
        ('1', 'Cobrar amanhã'),
        ('0', 'Não avisar'),
    ]
    frequencia_aviso = models.CharField(max_length=2, choices=AVISOS, default='7')

    criado_em = models.DateTimeField(auto_now_add=True)  # <- opcional, para ordenação

    def __str__(self):
        return f"{self.nome_cliente} - {self.servico}"
