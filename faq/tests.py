import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import FAQ

@pytest.mark.django_db
class TestFAQ:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def faq_item(self):
        return FAQ.objects.create(
            question="What is this?",
            answer="This is a test FAQ.",
            question_hi="यह क्या है?",
            answer_hi="यह एक परीक्षण FAQ है।"
        )

    def test_create_faq(self, api_client):
        url = reverse('faq-list')
        data = {
            'question': 'Test Question',
            'answer': 'Test Answer'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_faq_list(self, api_client, faq_item):
        url = reverse('faq-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_faq_translated(self, api_client, faq_item):
        url = reverse('faq-list') + '?lang=hi'
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['question'] == "यह क्या है?"