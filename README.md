## Nginx

`nginx` має стояти на сервері поза Docker. У Docker лишаються тільки Django (`gunicorn`) і база.

Запуск:

```bash
docker compose up --build
```

Після старту:

- Django застосунок слухає тільки `127.0.0.1:8000` на сервері
- статика збирається в локальну директорію `./staticfiles`
- серверний `nginx` проксіює запити на `127.0.0.1:8000` і віддає `/static/` напряму

Конфіг `nginx` лежить у `nginx.conf`.

Його треба покласти, наприклад, у `/etc/nginx/sites-available/django-pub-hackathon` і змінити шлях в `alias`:

```nginx
alias /srv/django-pub-hackathon/staticfiles/;
```

на фактичний абсолютний шлях до директорії `staticfiles` на сервері.
