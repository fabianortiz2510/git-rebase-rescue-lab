import pandas as pd
import numpy as np
from dateutil import parser

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