import pandas as pd
import numpy as np

def advanced_cleaning_with_pandas(data_list):
    """Convierte una lista a Serie de Pandas para eliminar duplicados y nulos rápidamente."""
    s = pd.Series(data_list)
    return s.dropna().drop_duplicates().tolist()

def normalize_scales(numbers):
    """Usa NumPy para normalizar una lista de números entre 0 y 1."""
    arr = np.array(numbers)
    if arr.size == 0: return []
    return ((arr - arr.min()) / (arr.max() - arr.min())).tolist()

def filter_by_length(items, min_length=3):
    """
    Filtra una lista devolviendo solo los elementos que 
    tienen una longitud mayor o igual al mínimo especificado.
    """
    return [item for item in items if len(str(item)) >= min_length]