# learning-postgres
PostgreSQL local com Docker Compose para estudos.

## Subir o banco
```bash
docker compose up -d
Ver status

docker compose ps
Ver logs

docker compose logs -f postgres
Conectar no psql dentro do container

docker compose exec postgres psql -U postgres -d learning_postgres
Parar containers

docker compose down
Resetar tudo (inclui dados do volume)

docker compose down -v
Connection string (localhost)