# Mysite

## Instructions to run the Project

* Run the server using this command `docker-compose up -d --build`

* For database migration run this command `docker-compose exec server pdm run alembic upgrade head`