from models import db
from models import User

db.create_all()

admin = User('admin', 'admin123')
guest = User('guest', 'guest123')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

users = User.query.all()
print users