import re

def preprocess_text(text):
    text = text.lower()  
    text = re.sub(r'[^a-zA-Z\s]', '', text)  
    words = text.split()  
    return words
