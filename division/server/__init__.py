from flask import Flask

from server.routes.views import routes_blueprint


def create_app(
        name: str = __name__,
        config: str = 'flask.cfg'
):

    app = Flask(
        name,
        template_folder='static/templates',
        instance_relative_config=True
    )

    app.config.from_pyfile(config)

    app.register_blueprint(routes_blueprint)

    return app
