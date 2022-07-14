from rest_framework import serializers

from article.models import Article as ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArticleModel
        fields = ["user", "title","content",]