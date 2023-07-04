import os
import unittest
import click

from app import blueprint
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.main import create_app, db

from app.main.model import status_model


app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
app.register_blueprint(blueprint)

# CORS SETUP
CORS(app, resources={r"/*": {"origins": "*"}})

app.app_context().push()

# DB SETUP
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, test=test)


@app.cli.command()
def run():
    app.run()


@app.cli.command()
# @click.option('--coverage/--no-coverage', default=False, help='Enable code coverage')
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@app.cli.command()
@click.option("--length", default=25, help="Profile stack length")
@click.option("--profile-dir", default=None, help="Profile directory")
def profile(length, profile_dir):
    """Start the application under the code profiler."""
    # ...


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # ...
