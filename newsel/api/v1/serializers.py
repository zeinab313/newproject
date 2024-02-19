from rest_framework import serializers
from ...models import Post

class PostSerializer(serializers.ModelSerializer):
        
    class Meta:
        model=Post
        fields=['id', 'folder_name', 'author', 'publisher', 'title', 'meta_kword',
                  'content', 'snippet','image_url', 'url', 
                  'media_description', 'type_of_news', 'tags',
                  'supervisor_to_confirm', 'source_website',
                  'published_date']
        
class SearchCrawlSerializer(serializers.ModelSerializer):
     folder_name=serializers.CharField(required=True)
     class Meta:
        model=Post
        fields=['folder_name']
     def validate(self, attrs):
        if attrs.get('foldrer_name'):
            pass
       

    
    
    