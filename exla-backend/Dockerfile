FROM python:3.7

WORKDIR /src

COPY src/requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY src/app /app

CMD ["python","/app/main.py"]