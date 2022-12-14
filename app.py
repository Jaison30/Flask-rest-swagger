from flask_migrate import Migrate

from app.models import User
from . import create_app, db
from app.models import User, Role, Post


app = create_app('default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)
