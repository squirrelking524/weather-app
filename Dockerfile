FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY weather.py .
CMD ["python", "weather.py", "--city", "Marysville"]
