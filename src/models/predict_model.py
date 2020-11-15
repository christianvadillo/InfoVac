import joblib
from src.models.support_functions import NormalizeTextTransformer
from typing import List

file = '../../models/svm_pipeline_10_Nov_2020_10_30.sav'


def is_list_of_strings(lst: List) -> bool:
    if lst and isinstance(lst, list):
        return all(isinstance(elem, str) for elem in lst)
    else:
        return False


def predict(text: List[str]):
    assert is_list_of_strings(text), 'Input must be a list of strings'
    model = joblib.load(file)
    print(model.predict_proba(text))


if __name__ == '__main__':
    predict(['Esto es un texto de prueba para nuestro clasificador svm para detectar información poco confiable',
             'Una receta con aspirinas, jengibre, canela, limón, cebolla y miel cura el COVID-19',
             "Circularon en redes sociales supuestas declaraciones del actor argentino sobre el caso de la joven cordobesa que no pudo ver a su padre antes de morir de cáncer en Córdoba, debido a las medidas de restricción de la pandemia. ”La chica pudo ver a su padre por wassap. No es que no la vio” (sic), es la frase que se le atribuye a Rizzo y que es falsa, ya que no hay registros públicos de que haya hecho tales afirmaciones. ",
            ])