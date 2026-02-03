from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response({
        'message': 'Welcome to TaskManagement APIs',
        'version': 'v1',
        'endpoints': {
            'authentication': {
                'register': '/api/v1/auth/register/',
                'login': '/api/v1/auth/login/',
                'refresh': '/api/v1/auth/refresh/',
                'verify': '/api/v1/auth/verify/',
            },
            'categories': {
                'list': '/api/v1/categories/',
                'detail': '/api/v1/categories/{id}/',
            },
            'tasks': {
                'list': '/api/v1/tasks/',
                'detail': '/api/v1/tasks/{id}/',
                'filters': '?status=PE&priority=2&category=1',
                'search': '?search=keyword',
                'ordering': '?ordering=-due_date',
            }
        },
        'documentation': 'https://github.com/Tathya-Dixit/Task-Management-APIs',
    })