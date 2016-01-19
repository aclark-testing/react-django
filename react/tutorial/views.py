from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentSerializer

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be created.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
