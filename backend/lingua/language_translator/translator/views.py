from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from googletrans import LANGUAGES, Translator

@api_view(['GET'])
def get_languages(request):
    return Response({'languages': LANGUAGES})

@api_view(['POST'])
def translate(request):
    try:
        # Get input text and selected languages
        data = request.data
        txt = data.get('text', '')
        c1 = data.get('src_lang', '')
        c2 = data.get('dest_lang', '')

        if txt:
            translator = Translator(service_urls=['translate.google.com'])

            # Translate the text
            result = translator.translate(txt, src=c1, dest=c2)
            translated_text = result.text

            return Response({'translated_text': translated_text})
    except Exception as e:
        return Response({'error': str(e)}, status=400)