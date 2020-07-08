from app.async_tasks.config import config


def start_something():
    config.logger.info('STARTING SOMETHING NEW')
    task = do_something.apply_async(countdown=0.2)
    return task.id


@config.worker.task
def do_something():
    config.logger.info('DOING SOMETHING')
    return True
