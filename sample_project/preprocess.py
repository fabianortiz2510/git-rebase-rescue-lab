import pandas as pd
import numpy as np
from dateutil import parser
import re
import string

def advanced_cleaning_with_pandas(data_list):
    """Convierte una lista a Serie de Pandas para eliminar duplicados y nulos rápidamente."""
    s = pd.Series(data_list)
    return s.dropna().drop_duplicates().tolist()

def normalize_scales(numbers):
    """Usa NumPy para normalizar una lista de números entre 0 y 1."""
    arr = np.array(numbers)
    if arr.size == 0: return []
    return ((arr - arr.min()) / (arr.max() - arr.min())).tolist()

def standardize_dates(date_strings):
    """Usa python-dateutil para convertir diversos formatos de fecha a ISO estándar."""
    standard_dates = []
    for date in date_strings:
        try:
            standard_dates.append(parser.parse(date).isoformat())
        except:
            continue
    return standard_dates

def clean_text_native(text_list):
    """
    Limpia una lista de strings usando solo la librería estándar de Python.
    Elimina puntuación, números y espacios extra.
    """
    cleaned_data = []
    # Creamos un patrón para identificar signos de puntuación
    punctuation_pattern = str.maketrans('', '', string.punctuation)
    
    for text in text_list:
        if not isinstance(text, str):
            continue
        
        # 1. Convertir a minúsculas
        text = text.lower()
        # 2. Eliminar puntuación usando la tabla de traducción
        text = text.translate(punctuation_pattern)
        # 3. Eliminar números usando expresiones regulares
        text = re.sub(r'\d+', '', text)
        # 4. Eliminar espacios en blanco extra
        text = text.strip()
        
        if text:
            cleaned_data.append(text)
            
    return cleaned_data