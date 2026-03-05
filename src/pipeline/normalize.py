import unicodedata
import re

def normalize_text(text): #linha a linha 

    text = text.lower() # minúsculas

    text = unicodedata.normalize('NFD', text) 
    text = text.encode('ascii', 'ignore').decode("utf-8") #tira acentos

    text = re.sub(r'[^a-z0-9\s]', ' ', text) # remove caracteres que nao sejam letras ou numeros e substitui por espaços

    text = re.sub(r'\s+', ' ', text).strip() #ajusta espaços

    return text