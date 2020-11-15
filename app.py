from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn
from src.models.predict_model import predict, explain

app = FastAPI()
# model = joblib.load('models/svm_pipeline_10_Nov_2020_13_10.sav')
# class_names = {0: 'no confiable', 1:'confiable'}


class Input(BaseModel):
    text : str


@app.get("/")
def main():
    return 'AAAAAAAAAAAAA'


@app.post("/predict/{Input}")
def predict_(input: Input):
    probas = predict([input.text]).round(3)
    # explainer = LimeTextExplainer(class_names=class_names)
    # explain = explainer.explain_instance(text, model.predict_proba)
    response = {'texto': input.text,
            'proba_no_confiable': probas[0, 0],
            'proba_confiable': probas[0, 1]}

    return response


@app.post("/explain/{Input}")
def explain_(input: Input):
    return explain([input.text])


    # return {'texto': text,
    #         'proba_no_confiable': probas[0, 0],
    #         'proba_confiable': probas[0, 1],
    #         'conf_words': [line[0] for line in explain.as_list() if line[1] > 0],
    #         'no_conf_words': [line[0] for line in explain.as_list() if line[1] < 0]
    #         }

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8001)


# To run in terminal
#uvicorn app:app --port 8001 --reload
