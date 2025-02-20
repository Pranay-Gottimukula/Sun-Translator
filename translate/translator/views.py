from django.shortcuts import render
from googletrans import Translator
# Create your views here.

def translate_text(request):
    translated_text = None

    if request.method == "POST":
        text = request.POST.get("text")
        target_lang = request.POST.get("target_lang")

        translator = Translator()
        translated_text = translator.translate(text, dest=target_lang).text

    return render(request, "translator/index.html", {"translated_text": translated_text})
