from flask import request, jsonify
from config import app, db
from models import Contact


if __name__ == "__main__":
    # Check if the script is being run directly (not imported as a module)
    with app.app_context():
        # Create an application context which is necessary for database operations
        db.create_all()
        # Create all tables defined in SQLAlchemy models if they don't exist already
    app.run(debug=True)
    # Run the Flask application with debugging enabled for easier development
