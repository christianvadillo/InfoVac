FROM python:3.7

WORKDIR /infovac-app

RUN pip install spacy
RUN pip install nltk
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install lime
RUN pip install https://github.com/explosion/spacy-models/releases/download/es_core_news_md-3.0.0a0/es_core_news_md-3.0.0a0.tar.gz
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt


COPY ./app ./app
COPY ./models ./models
COPY ./src ./src
COPY ./__init__.py ./__init__.py

ENV PYTHONPATH /infovac-app

EXPOSE 8001

CMD ["python", "./app/main.py"]


# To run in terminal
#uvicorn app:app --port 8001 --reload
# docker run -p 8001:8001 infovac-app