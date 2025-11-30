FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "sast.py", "scan", "tests", "--json", "report.json", "--html", "report.html"]
