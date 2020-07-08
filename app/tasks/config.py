from celery import Celery

worker = None

def make_worker(app):
    global worker
    worker = Celery(
        app.import_name,
        backend=app.config['REDIS_URL'],
        broker=app.config['REDIS_URL']
    )
    worker.conf.update(app.config)

    worker.conf.task_acks_late = True
    worker.conf.worker_prefetch_multiplier = 1
    worker.conf.task_routes = {
        'app.tasks.storage_files.archive_files': {'queue': 'indexing'}
    }

    TaskBase = worker.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    worker.Task = ContextTask


def register_tasks(worker):
    pass
