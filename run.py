from app import app, db
from app.models import User, Team, Name, Company

@app.shell_context_processor
def make_context():
    return dict(
        db=db,
        User=User,
        Team=Team,
        Name=Name,
        Company=Company
    )