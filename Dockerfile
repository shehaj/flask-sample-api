FROM python:3.9.18-slim

WORKDIR /application

COPY api.py /application

RUN pip install flask psutil requests

EXPOSE 5000

CMD ["flask", "--app", "api", "run", "--host=0.0.0.0"]


