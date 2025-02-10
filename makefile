# Nombre del servicio en docker-compose.yml (ajústalo si es diferente)
DOCKER_BACKEND=docker exec -it django_backend
DOCKER_FRONTEND=docker exec -it vue_frontend

# Comando para migraciones de Django
migrate:
	$(DOCKER_BACKEND) python manage.py makemigrations
	$(DOCKER_BACKEND) python manage.py migrate

# Comando para crear superusuario en Django
create-superuser:
	$(DOCKER_BACKEND) python manage.py createsuperuser

# Iniciar el servidor de desarrollo de Vue
frontend-dev:
	$(DOCKER_FRONTEND) npm run dev

# Ver logs de Django
logs-backend:
	docker logs -f django_backend

# Ver logs de Vue
logs-frontend:
	docker logs -f vue_frontend

# Levantar los contenedores
up:
	docker-compose up -d

# Detener los contenedores
down:
	docker-compose down

# Reconstruir imágenes y levantar contenedores
rebuild:
	docker-compose up --build -d
