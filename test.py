from transformers import pipeline
transloter = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")
transloter('Меня зовут Стас')