FROM python:latest
ADD . /app
WORKDIR ./app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python main.py
