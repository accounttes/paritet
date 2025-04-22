from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

class ImageViewSet(viewsets.ViewSet):
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request):
        if 'image' not in request.FILES:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        image = request.FILES['image']
        description = request.data.get('description', '')
        
        # Save the image
        path = default_storage.save(f'images/{image.name}', ContentFile(image.read()))
        
        return Response({
            'id': path,
            'description': description,
            'url': f'/media/{path}'
        }, status=status.HTTP_201_CREATED)

    def list(self, request):
        # This would typically list all images from the database
        return Response([], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            default_storage.delete(f'images/{pk}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND) 