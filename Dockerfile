# Python
FROM python:3.10-slim

# Nastavení pracovního adresáře
WORKDIR /IT4-projekt

# Zkopíruje se soubor requirements.txt do kontejneru
COPY requirements.txt /app/

# Nainstalování všech závislotí
RUN pip install --no-cache-dir -r requirements.txt

# Zkopíruje se celý projekt do pracovního adresáře v kontejneru
COPY . /IT4-projekt/

# port 8000 pro Django server
EXPOSE 8000

# Příkaz, který se spustí při startu kontejneru
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
