from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protegido(request):
    return Response({
        'message': f'Bem-vindo, {request.user.username}! Você está autenticado com token.'
    })

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
