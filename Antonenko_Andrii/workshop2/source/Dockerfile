FROM python:3.6.1-alpine
RUN pip install --upgrade pip
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
RUN export FLASK_ENV=prod
CMD ["python", "main.py"]
