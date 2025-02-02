from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'en')
        return context

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faq_list_{lang}'
        
        # Try to get cached response
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response)

        # Generate new response
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data
        
        # Cache the response for 24 hours
        cache.set(cache_key, response_data, timeout=86400)
        
        return Response(response_data)