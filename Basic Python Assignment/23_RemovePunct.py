import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

text = "Hello, world! How's it going?"
cleaned_text = remove_punctuation(text)
print(cleaned_text)