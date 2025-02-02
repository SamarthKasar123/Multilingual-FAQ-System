from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    # Language-specific fields
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    def get_translated_field(self, field_name, lang):
        # Check cache first
        cache_key = f'faq_{self.id}_{field_name}_{lang}'
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value

        # Get the translated field if it exists
        translated_field = f'{field_name}_{lang}'
        if hasattr(self, translated_field) and getattr(self, translated_field):
            value = getattr(self, translated_field)
        else:
            # Fallback to English and translate
            original_value = getattr(self, field_name)
            translator = Translator()
            try:
                translation = translator.translate(original_value, dest=lang)
                value = translation.text
                # Store the translation
                setattr(self, translated_field, value)
                self.save()
            except Exception:
                value = original_value

        # Cache the result
        cache.set(cache_key, value, timeout=86400)  # Cache for 24 hours
        return value

    def get_question(self, lang='en'):
        if lang == 'en':
            return self.question
        return self.get_translated_field('question', lang)

    def get_answer(self, lang='en'):
        if lang == 'en':
            return self.answer
        return self.get_translated_field('answer', lang)