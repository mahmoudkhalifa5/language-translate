# Mini Language Translator

# قاعدة البيانات (dictionary)
translations = {
    "hello": {
        "spanish": "hola",
        "french": "bonjour",
        "german": "hallo",
        "arabic": "ابحرم"
    },
    "goodbye": {
        "spanish": "adiós",
        "french": "au revoir",
        "german": "tschüss"
    },
    "thank you": {
        "spanish": "gracias",
        "french": "merci",
        "german": "danke"
    },
    "yes": {
        "spanish": "sí",
        "french": "oui",
        "german": "ja"
    },
    "no": {
        "spanish": "no",
        "french": "non",
        "german": "nein"
    }
}

# إدخال المستخدم
word = input("Enter an English word: ").lower()
language = input("Translate to (spanish/french/german/arabic): ").lower()

# الترجمة
if word in translations:
    if language in translations[word]:
        print("Translation:", translations[word][language])
    else:
        print("Language not supported.")
else:
    print("Word not found in dictionary.")