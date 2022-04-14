build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
    docker compose -f local.yml up -d

down:
    docker compose -f local.yml down

show_logs:
    docker compose -f local.yml logs

migrate:
    docker compose -f local.yml run --rm api python manage.py migrate

makemigrations:
    docker compose -f local.yml run --rm api python manage.py makemigrations

collectstatic:
    docker compose -f --rm api python manage.py collectstatic --no-input --clear

superuser:
    docker compose -f local.yml run --rm api python manage.py createsuperuser

down-v:
    docker compose -f local.yml down -v

volume:
    docker volume inspect celery_prac_local_postgres_data

authors-db:
    docker compose -f local.yml exec celery_prac_postgres psql --username=cjhadmin --dbname=authors-live

flake8:
    docker compose -f local.yml exec api flake8 .

black-check:
    docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
    docker compose -f local.yml exec api black --diff --exclude=migrations .

black:
    docker compose -f local.yml exec api black --exclude=migrations .

isort-check:
    docker compose -f local.yml exec api isort . --check-only --skip env --skip migrations

isort-diff:
    docker compose -f local.yml exec api isort . --diff --skip env --skip migrations

isort:
    docker compose -f local.yml exec api isort . --skip env --skip migrations
