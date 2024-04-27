from deep_translator import GoogleTranslator
to_translate = input("Enter a word: ")
translated = GoogleTranslator(source='en', target='ru').translate(to_translate)

print(translated)