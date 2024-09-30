from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print("Welcome to the Language text Translator!")
    
    # User input for text
    sample_text = input("Enter the text you want to translate: ")
    
    # User input for target language
    target_language = input("Enter the language code (e.g., 'fr' for French): ")
    
    # Translate and display the result
    translated_text = translate_text(sample_text, target_language)
    print(f"\nOriginal: {sample_text}")
    print(f"Translated: {translated_text}")
