Данный шаблон проекта предназначен для быстрого развертывания проекта на Django с PosgreSQL:

`
django-admin startproject --template=/opt/django_template --name=settings.py $DJANGO_PROJECT_NAME /app
`

Содержит тестовый проект для отладки сборки с Docker (+docker compose), Nginx, Gunicorn, PosgreSQL. С загрузкой и сохранением файлов, миграциями.