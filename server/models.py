from config import db
from datetime import datetime

# Data to be fed into the database.

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), unique = False, nullable=False)
    last_name = db.Column(db.String(25), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime,nullable = False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,nullable = False, default=datetime.utcnow, onupdate=datetime.utcnow)


#     

