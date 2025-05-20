from django.shortcuts import render
from deep_translator import GoogleTranslator

def counter(request):
    word_count = None
    translation = None
    text = ""

    if request.method == "POST":
        text = request.POST.get("input_text", "")
        language = request.POST.get("language")

        # Підрахунок слів
        word_count = len(text.split())

        # Переклад через GoogleTranslator з deep-translator
        if language:
            try:
                translation = GoogleTranslator(target=language).translate(text)
            except Exception as e:
                translation = f"Error during translation: {e}"

    context = {
        "word_count": word_count,
        "translation": translation,
        "original_text": text,
    }
    return render(request, 'index.html', context)
