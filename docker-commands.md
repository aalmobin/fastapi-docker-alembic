## For database backup
```bash
docker exec -t <db-container-name> pg_dump -U <db_user> <db_name> | gzip > db_backup.sql.gz
```

## For database restore
```bash
gunzip < db_backup.sql.gz | docker exec -i <db-container-name> psql -U <db_user> <db_name>
```

## Delete all containers images and volume for a docker-compose file
```bash
docker-compose down --volumes --rmi all 
```