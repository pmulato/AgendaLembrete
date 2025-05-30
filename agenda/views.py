from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protegido(request):
    return Response({'message': f'Bem-vindo, {request.user.username}! Você está autenticado com token.'})
