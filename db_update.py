# sandbox for database stuff

from project import db
from project.models import *

user = User.query.first()
user.is_admin = True

db.session.commit()