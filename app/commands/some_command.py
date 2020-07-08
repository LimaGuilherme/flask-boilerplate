# -*- coding: utf-8 -*-


def register_command(app):

    @app.cli.command()
    def do_something():
        print('Hello My Friend')