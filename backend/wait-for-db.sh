#!/bin/bash

# Esperar a que MySQL esté disponible
until mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e 'SELECT 1'; do
  echo "Esperando a MySQL..."
  sleep 5
done

# Verificar si las migraciones ya se han aplicado (basado en el estado de la base de datos)
if python manage.py showmigrations | grep -q '\[ \]'; then
  echo "Hay migraciones pendientes. Ejecutando migraciones..."
  python manage.py migrate
else
  echo "Las migraciones ya han sido aplicadas. Saltando..."
fi

# Verificar si el superusuario ya existe
if python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='admin').exists())" | grep -q 'True'; then
  echo "El superusuario ya existe. Saltando..."
else
  echo "Creando superusuario..."
  python manage.py createsuperuser --noinput
fi

# Ejecutar el servidor
python manage.py runserver 0.0.0.0:8000
