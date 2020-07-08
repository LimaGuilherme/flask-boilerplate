from app.commands import some_command


def register(web_app):
    some_command.register_command(web_app)
