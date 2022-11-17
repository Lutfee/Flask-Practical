FROM python:latest
ADD main.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python main.py
