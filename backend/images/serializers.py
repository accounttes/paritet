from rest_framework import serializers
from .models import Image
import base64

class ImageSerializer(serializers.ModelSerializer):
    image_base64 = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'image', 'description', 'created_at', 'updated_at', 'image_base64']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_image_base64(self, obj):
        if obj.image:
            with open(obj.image.path, 'rb') as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        return None

    def create(self, validated_data):
        image_base64 = self.context['request'].data.get('image_base64')
        if image_base64:
            # Remove the data URL prefix if present
            if 'base64,' in image_base64:
                image_base64 = image_base64.split('base64,')[1]
            
            # Decode base64 to binary
            image_data = base64.b64decode(image_base64)
            
            # Create a new file in memory
            from django.core.files.base import ContentFile
            image_file = ContentFile(image_data, name='image.jpg')
            
            # Add the file to validated_data
            validated_data['image'] = image_file
        
        return super().create(validated_data) 