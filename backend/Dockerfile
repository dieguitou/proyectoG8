# Usa Python como imagen base
FROM python:3.12

# Instalar dependencias del sistema, incluyendo el cliente de MySQL (mariadb-client-core)
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    mariadb-client-core \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del backend al contenedor
COPY . .

# Expone el puerto de Django
EXPOSE 8000

# Comando para iniciar Django con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "inmuebles.wsgi:application"]
