from rest_framework.exceptions import APIException

class TranslationError(APIException):
    status_code = 503
    default_detail = 'Translation service temporarily unavailable.'
    default_code = 'translation_error'

class CacheError(APIException):
    status_code = 503
    default_detail = 'Cache service temporarily unavailable.'
    default_code = 'cache_error'