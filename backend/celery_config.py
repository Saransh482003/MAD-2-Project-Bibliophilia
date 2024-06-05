from celery import Celery, Task
from flask import Flask


def celery_init_app(app: Flask) -> Celery:
    celery_app = Celery(app.name)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
