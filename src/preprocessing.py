import re
import string
import emoji

def advanced_text_preprocessing(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'\d+', '[ANGKA]', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    singkatan = {
        'dgn': 'dengan',
        'yg': 'yang',
        'utk': 'untuk'
    }
    
    words = text.split()
    processed_words = [singkatan.get(word, word) for word in words]
    text = ' '.join(processed_words)
    
    text = emoji.replace_emoji(text, replace='')
    text = ' '.join(text.split())
    
    return text