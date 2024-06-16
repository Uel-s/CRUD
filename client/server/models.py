from config import db
import pytz
from datetime import datetime
from sqlalchemy import  DateTime  # Import the required classes from SQLAlchemy

EAT = pytz.timezone('Africa/Nairobi')

def current_eat_time():
    return datetime.now(EAT)

# Data to be fed into the database.
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), unique=False, nullable=False)
    last_name = db.Column(db.String(25), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=current_eat_time)
    updated_at = db.Column(DateTime, nullable=False, default=current_eat_time, onupdate=current_eat_time)

    # A function to convert our db info to python dictionary and return it as json data which can be passed to an API.
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,  # camelCase for js(firstName) and snake_case for python(first_name)
            "lastName": self.last_name,
            "email": self.email
        }
