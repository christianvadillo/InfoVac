import joblib
from src.models.support_functions import NormalizeTextTransformer
from typing import List

file = '../../models/svm_pipeline_10_Nov_2020_10_30.sav'


def is_list_of_strings(lst):
    if lst and isinstance(lst, list):
        return all(isinstance(elem, str) for elem in lst)
    else:
        return False


def predict(text: List[str]):
    assert is_list_of_strings(text), 'Input must be a list of strings'
    model = joblib.load(file)
    print(model.predict_proba(text))


if __name__ == '__main__':
    predict(['Esto es un texto de prueba para nuestro clasificador svm para detectar información poco confiable'])