FROM python:3.7-alpine
LABEL app=python
WORKDIR /app
COPY . /app
RUN python -m pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
# CMD ["python", "app.py"]