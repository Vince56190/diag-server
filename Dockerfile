# Utilise Python 3.11
FROM python:3.11-slim

# Copie le contenu du dépôt dans le conteneur
WORKDIR /app
COPY . /app

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Indique à Fly d'exposer le port 8080
EXPOSE 8080

# Lance l'application Flask
CMD ["gunicorn", "-b", "0.0.0.0:8080", "server:app"]
